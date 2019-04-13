import asyncio
from collections import defaultdict

from sanic import Sanic
from sanic.response import json
from elasticsearch_async import AsyncElasticsearch


def get_client():
    client = AsyncElasticsearch(hosts=['http://222.85.141.99'])
    return client


app = Sanic()


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
            "indices": indices_per_node[node["name"]],
            "isMaster": node["master"] == "*",
            "ip": node["ip"],
            "role": node["node.role"],
            "metrics": {
                "CPUPercent": float(node["cpu"]),
                "heapPercent": float(node["heap.percent"]),
                "load1Percent": float(node["load_1m"]) / 4  # TODO: Count CPUs
            }
        })

    return json(nodes_result)

# // metrics: {
#             // heapPercent: 15,
# // diskPercent: 45,
# // CPUPercent: 65,
# // load1Percent: 4
#                  //}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
