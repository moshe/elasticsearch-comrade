from elasticsearch import TransportError
from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

rest_bp = Blueprint('rest')


def format_es_exception(e: TransportError):
    return json({"status_code": e.status_code,
                 "error": e.error,
                 "info": e.info})


@rest_bp.route('/query', methods=['POST'])
async def close_index(request: Request) -> HTTPResponse:
    client = get_client(request)
    body = request.json['body']
    method = request.json['method']
    path = request.json['path']
    try:
        resp = await client.transport.perform_request(method, path, body=body)
    except TransportError as e:
        return format_es_exception(e)
    return json(resp)
