from collections import defaultdict

from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

alias_bp = Blueprint('alias')


def format_alias_addition(action: dict) -> dict:
    data = {
        "index": action['index'],
        "alias": action['alias']
    }
    if action.get("filter") != {} and action.get("filter") not in {"", None}:
        data["filter"] = action["filter"]
    if action.get("searchRouting") not in {"", None}:
        data["search_routing"] = action["searchRouting"]
    if action.get("indexRouting") not in {"", None}:
        data["index_routing"] = action["indexRouting"]

    return {action['action']: data}


async def get_index_aliases(request: Request) -> dict:
    client = get_client(request)
    aliases = await client.cat.aliases(format='json')
    aliases_by_index = defaultdict(list)
    for alias in aliases:
        aliases_by_index[alias['index']].append(alias['alias'])
    return dict([(x, sorted(aliases_by_index[x])) for x in aliases_by_index])


@alias_bp.route('/batch', methods=['POST'])
async def create_alias(request: Request) -> HTTPResponse:
    client = get_client(request)
    actions = request.json['actions']
    await client.indices.update_aliases(
        {"actions": [format_alias_addition(action) for action in actions]}
    )
    return json({"status": "ok"})


@alias_bp.route('/list')
async def get_aliases(request: Request) -> HTTPResponse:
    client = get_client(request)
    aliases = await client.cat.aliases(format='json')
    response = defaultdict(list)
    for x in aliases:
        response[x['alias']].append(x['index'])
    return json(response)
