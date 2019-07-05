from sanic.response import json
from sanic import Blueprint

from connections import get_client

template_bp = Blueprint('template')


@template_bp.route('/list')
async def list_templates(request):
    client = get_client(request)
    templates = await client.indices.get_template()
    return json([dict(name=x, **templates[x]) for x in templates])
