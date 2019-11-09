from collections import ChainMap
from copy import deepcopy

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client
from ..elasticsearch_assets import get_index_settings_docs

index_bp = Blueprint('index')


@index_bp.route('/<index>/close')
async def close_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.close(index=index, expand_wildcards='none')
    return json({"status": "ok"})


@index_bp.route('/<index>/open')
async def open_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.open(index=index, expand_wildcards='none')
    return json({"status": "ok"})


@index_bp.route('/<index>/stats')
async def index_stats(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    return json(await client.indices.stats(index=index))


@index_bp.route('/<index>/dynamicSettings')
async def dynamic_settings(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    all_settings = await client.indices.get_settings(index=index, flat_settings=True, include_defaults=True)
    chained = ChainMap(*all_settings[index].values())
    sections = deepcopy(get_index_settings_docs())
    for section in sections:
        for setting in section['settings']:
            if setting['name'] in chained:
                setting['value'] = chained[setting['name']]
    return json(sections)


@index_bp.route('/<index>/settings')
async def index_settings(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    return json(await client.indices.get_settings(index=index, flat_settings=True))


@index_bp.route('/<index>/settings', methods=['POST'])
async def set_index_settings(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    return json(await client.indices.put_settings(dict(request.json), index))


@index_bp.route('/<index>/mapping')
async def get_mapping(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    return json(await client.indices.get_mapping(index=index))


@index_bp.route('/<index>/head')
async def head_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    content = await client.search(index=index)
    return json(x['_source'] for x in content['hits']['hits'])


@index_bp.route('/<index>/flush')
async def flush_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.flush(index=index)
    return json({"status": "ok"})


@index_bp.route('/<index>/forcemerge')
async def merge_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.forcemerge(index=index)
    return json({"status": "ok"})


@index_bp.route('/<index>/delete')
async def delete_index(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.delete(index=index)
    return json({"status": "ok"})


@index_bp.route('/<index>/clearCache')
async def clear_cache(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.clear_cache(index=index, allow_no_indices=False)
    return json({"status": "ok"})


@index_bp.route('/graveyard')
async def graveyard(request: Request) -> HTTPResponse:
    client = get_client(request)
    resp = await client.cluster.state(metric='metadata')
    return json(resp['metadata']['index-graveyard']['tombstones'])


@index_bp.route('/<index>/body')
async def get_body(request: Request, index: str) -> HTTPResponse:
    client = get_client(request)
    current_index_settings = (await client.indices.get(index))[index]
    if 'index' in current_index_settings['settings']:
        current_index_settings['settings']['index'].pop('creation_date', None)
        current_index_settings['settings']['index'].pop('uuid', None)
        current_index_settings['settings']['index'].pop('version', None)
        current_index_settings['settings']['index'].pop('provided_name', None)
    return json(current_index_settings)
