import asyncio
from collections import defaultdict

from elasticsearch_async import AsyncElasticsearch

from sanic import Sanic
from sanic.response import json


def get_client():
    client = AsyncElasticsearch(hosts=['http://222.85.141.99'])
    return client


app = Sanic()


def format_index_data(data):
    return {
        "primaries": int(data["pri"]),
        "replicas": int(data["rep"]),
        "status": data["status"],
        "docsCount": int(data["docs.count"]),
        "docsDeleted": int(data["docs.deleted"]),
        "storeSize": data["store.size"],
        "data": data
    }


@app.route('/api/v1/shards_grid')
async def indices_stats(request):
    indices, shards, nodes = await asyncio.gather(get_client().cat.indices(format='json'),
                                                  get_client().cat.shards(format='json'),
                                                  get_client().cat.nodes(format='json'))
    indices_per_node = defaultdict(lambda: defaultdict(lambda: {'replicas': [], 'primaries': []}))
    for shard in shards:
        if shard['prirep'] == 'p':
            shard_type = 'primaries'
        elif shard['prirep'] == 'r':
            shard_type = 'replicas'
        else:
            raise RuntimeError('Unknown shard type %s' % shard['prirep'])
        indices_per_node[shard['node']][shard['index']][shard_type].append(int(shard['shard']))

    nodes_result = []
    for node in nodes:
        nodes_result.append({
            "name": node["name"],
            "indices": dict(sorted(indices_per_node[node["name"]].items())),
            "isMaster": node["master"] == "*",
            "ip": node["ip"],
            "role": node["node.role"],
            "metrics": {
                "CPUPercent": float(node["cpu"]),
                "heapPercent": float(node["heap.percent"]),
                "load1Percent": float(node["load_1m"]) / 4  # TODO: Count CPUs
            }
        })

    return json({
        "nodes": sorted(nodes_result, key=lambda x: x["name"]),
        "indices": dict([(x['index'], format_index_data(x)) for x in indices])
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
