from sanic.response import json
from sanic import Blueprint

from connections import get_client

cluster_bp = Blueprint('cluster')


@cluster_bp.route('/reroute_shards', methods=['POST'])
async def reroute_shard(request):
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
async def set_allocation(request, operation):
    assert operation in {"all", "primaries", "new_primaries", "none"}
    client = get_client(request)
    response = await client.cluster.put_settings(body={"transient": {"cluster.routing.allocation.enable": operation}})
    assert response.get('acknowledged') is True
    return json({"status": "ok"})
