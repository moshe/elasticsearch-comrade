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


@index_bp.route('/<index>/stats')
async def open_index(request, index):
    client = get_client()
    return json(await client.indices.stats(index=index))


@index_bp.route('/<index>/settings')
async def open_index(request, index):
    client = get_client()
    return json(await client.indices.get_settings(index=index, flat_settings=True))


@index_bp.route('/<index>/mapping')
async def open_index(request, index):
    client = get_client()
    return json(await client.indices.get_mapping(index=index))


@index_bp.route('/<index>/head')
async def open_index(request, index):
    client = get_client()
    content = await client.search(index=index)
    return json(x['_source'] for x in content['hits']['hits'])
