from sanic.response import json
from sanic import Blueprint

from connections import get_client

terminal_bp = Blueprint('terminal')


@terminal_bp.route('/query', methods=['POST'])
async def close_index(request):
    client = get_client()
    body = request.json['body']
    method = request.json['method']
    url = request.json['url']
    resp = await client.transport.perform_request(method, url, body=body)
    return json(resp)

