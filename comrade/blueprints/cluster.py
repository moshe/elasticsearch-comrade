from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

cluster_bp = Blueprint('cluster')


@cluster_bp.route('/reroute_shards', methods=['POST'])
async def reroute_shard(request: Request) -> HTTPResponse:
    client = get_client(request)
    node = request.json['node']
    shards = request.json['shards']
    await client.cluster.reroute(
        body={"commands": [
            {"move": {"index": shard['index'], "shard": shard['id'], "from_node": shard['nodeName'], "to_node": node}}
            for shard in shards
        ]}
    )
    return json({"status": "ok"})


@cluster_bp.route('/allocation/<operation>', methods=['POST'])
async def set_allocation(request: Request, operation: str) -> HTTPResponse:
    assert operation in {"all", "primaries", "new_primaries", "none"}
    client = get_client(request)
    response = await client.cluster.put_settings(body={"transient": {"cluster.routing.allocation.enable": operation}})
    assert response.get('acknowledged') is True
    return json({"status": "ok"})


@cluster_bp.route('/info/<cluster_name>')
async def get_cluster_info(request: Request, cluster_name: str) -> HTTPResponse:
    client = get_client(None, cluster_name)
    await client.ping()

    response = await client.cluster.stats()
    try:
        jvm = 'mixed' if len(response['nodes']['jvm']['versions']) > 1 else response['nodes']['jvm']['versions'][0][
            'vm_name']
    # For some reasone es6.3.1 is missing jvm version
    except KeyError:
        jvm = 'unknown'
    return json({
        "name": response['cluster_name'],
        "versions": response['nodes']['versions'],
        "jvmName": jvm,
        "numNodes": response['_nodes']['total'],
        "status": response['status'],
        "docCount": response['indices']['docs']['count'],
        "storeSizeInBytes": response['indices']['store']['size_in_bytes']

    })
