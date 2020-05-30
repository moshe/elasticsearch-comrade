from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

template_bp = Blueprint('template')


@template_bp.route('/list')
async def list_templates(request: Request) -> HTTPResponse:
    client = get_client(request)
    templates = await client.indices.get_template()
    return json([dict(name=x, **templates[x]) for x in templates])


@template_bp.route('/<template>/delete')
async def delete_template(request: Request, template: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.delete_template(template)
    return json("ok")


@template_bp.route('/<template>/update', methods=['POST'])
async def update_template(request: Request, template: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.put_template(name=template, body=request.json, create=False)
    return json("ok")


@template_bp.route('/<template>/create', methods=['POST'])
async def create_template(request: Request, template: str) -> HTTPResponse:
    client = get_client(request)
    await client.indices.put_template(name=template, body=request.json, create=True)
    return json("ok")
