from collections import defaultdict
from sanic.response import json
from sanic import Blueprint

from connections import get_client

alias_bp = Blueprint('alias')


def format_alias_addition(index, alias):
    data = {
        "index": index,
        "alias": alias["alias"]
    }
    if alias.get("filter") != {} and alias.get("filter") not in {"", None}:
        data["filter"] = alias["filter"]
    if alias.get("searchRouting") not in {"", None}:
        data["search_routing"] = alias["searchRouting"]
    if alias.get("indexRouting") not in {"", None}:
        data["index_routing"] = alias["indexRouting"]

    return {"add": data}


async def get_index_aliases():
    client = get_client()
    aliases = await client.cat.aliases(format='json')
    aliases_by_index = defaultdict(list)
    for alias in aliases:
        aliases_by_index[alias['index']].append(alias['alias'])
    return dict([(x, sorted(aliases_by_index[x])) for x in aliases_by_index])


@alias_bp.route('/create', methods=['POST'])
async def create_alias(request):
    client = get_client()
    data = request.json
    await client.indices.update_aliases(
        {"actions": list([
            format_alias_addition(index, data) for index in data['indices']
        ])}
    )
    return json({"status": "ok"})
