from sanic.response import json
from sanic import Blueprint

from connections import get_client

index_bp = Blueprint('index')


@index_bp.route('/<index>/close')
async def close_index(request, index):
    client = get_client()
    await client.indices.close(index=index, expand_wildcards='none')
    return json({"status": "ok"})


@index_bp.route('/<index>/open')
async def open_index(request, index):
    client = get_client()
    await client.indices.open(index=index, expand_wildcards='none')
    return json({"status": "ok"})
