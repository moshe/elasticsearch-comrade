from asyncio import gather
from collections import defaultdict

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..blueprints.alias import get_index_aliases
from ..connections import get_client

views_bp = Blueprint('views')


def format_index_data(data: dict, aliases: dict) -> dict:
    append = {"aliases": []}
    if data['index'] in aliases:
        append["aliases"] = aliases[data['index']]
    if data['status'] == 'close':
        return dict(status=data["status"], **append)
    return dict({
        "primaries": int(data["pri"]),
        "replicas": int(data["rep"]),
        "status": data["status"],
        "docsCount": int(data["docs.count"] or 0),
        "docsDeleted": int(data["docs.deleted"] or 0),
        "storeSize": data["store.size"],
    }, **append)


async def get_cluster_info(request: Request) -> dict:
    client = get_client(request)
    [info], [docs], settings = await gather(client.cat.health(format='json'),
                                            client.cat.count(format='json'),
                                            client.cluster.get_settings(flat_settings=True))
    return {
        "relocatingShards": int(info['relo']),
        "initializingShards": int(info['init']),
        "unassignedShards": int(info['unassign']),
        "numOfPrimaryShards": int(info['pri']),
        "numOfReplicaShards": int(info["shards"]) - int(info['pri']),
        "numberOfNodes": int(info['node.total']),
        "numberOfDocs": int(docs['count']),
        "clusterName": info['cluster'],
        "clusterStatus": info['status'],
        "settings": {
            "allocation": settings['transient'].get('cluster.routing.allocation.enable', 'all')
        },
    }


async def get_nodes_info(request: Request) -> list:
    client = get_client(request)
    info = await client.nodes.stats(metric='jvm,os,fs')
    result = []
    for node_id, node in info['nodes'].items():
        result.append({
            "name": node["name"],
            "isMaster": False,
            "ip": node.get("ip", "no-ip"),
            "roles": node["roles"],
            "id": node_id,
            "metrics": {
                # Reduce precision in order to reduce render loops in UI
                "CPUPercent": int(node['os']['cpu']['percent']),
                "heapPercent": int(node['jvm']['mem']['heap_used_percent']),
                "load1Percent": int(float(node['os']['cpu']['load_average']['1m']) / 4),  # TODO: Count CPUs

                "diskPercent": int(
                    node['fs']['total']['available_in_bytes'] * 100 / node['fs']['total']['total_in_bytes'])
            }
        })
    return result


async def get_shards_info(request: Request) -> tuple:
    client = get_client(request)
    shards = await client.cat.shards(format='json')
    relocating_indices = list({shard['index'] for shard in shards if shard['state'] == 'RELOCATING'})
    recovery = await client.cat.recovery(index=relocating_indices, format='json')
    relocation_progress = {
        (recovery_data["index"], recovery_data["shard"]):
            int(float(recovery_data["bytes_recovered"]) * 100 / (int(recovery_data["bytes_total"]) or 1))
        for recovery_data in recovery if recovery_data["stage"] != "done" and recovery_data["bytes_total"]
    }
    return shards, relocation_progress


@views_bp.route('/shards_grid')
async def indices_stats(request: Request) -> HTTPResponse:
    client = get_client(request)
    indices, aliases, shards, nodes, cluster_info = await gather(client.cat.indices(format='json'),
                                                                 get_index_aliases(request),
                                                                 get_shards_info(request),
                                                                 get_nodes_info(request),
                                                                 get_cluster_info(request))
    shards, relocation_progress = shards
    cluster_info["numOfIndices"] = len(indices)
    indices_per_node = defaultdict(lambda: defaultdict(lambda: {'replicas': [], 'primaries': []}))
    unassigned_shards = defaultdict(lambda: {'replicas': [], 'primaries': []})
    for shard in shards:
        if shard['prirep'] == 'p':
            shard_type = 'primaries'
        elif shard['prirep'] == 'r':
            shard_type = 'replicas'
        else:
            raise RuntimeError('Unknown shard type %s' % shard['prirep'])
        data = {
            "shard": int(shard['shard']),
            "state": shard['state'],
        }
        node = shard['node']
        if shard['state'] == 'UNASSIGNED':
            unassigned_shards[shard['index']][shard_type] = sorted(
                unassigned_shards[shard['index']][shard_type] + [data],
                key=lambda x: x['shard'])
        if shard['state'] == 'RELOCATING':
            from_node, to_node = node.split(' -> ')
            node = from_node
            data['fromNode'] = to_node.split()[2]
            data['progress'] = relocation_progress.get((shard['index'], shard['shard']), 0)
        if shard['state'] == 'INITIALIZING':
            data['progress'] = relocation_progress.get((shard['index'], shard['shard']), 0)
        indices_per_node[node][shard['index']][shard_type].append(data)
        indices_per_node[node][shard['index']][shard_type].sort(key=lambda x: x['shard'])

    for node in nodes:
        node['indices'] = dict(sorted(indices_per_node[node["name"]].items()))

    indices = dict(sorted([(x['index'], format_index_data(x, aliases)) for x in indices]))
    for index in indices:
        if index in unassigned_shards:
            indices[index]['unassignedShards'] = unassigned_shards[index]

    return json({
        "nodes": sorted(nodes, key=lambda x: x["name"]),
        "indices": indices,
        "cluster": cluster_info,
    })
