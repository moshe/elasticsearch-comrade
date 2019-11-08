
from sanic import Blueprint
from sanic.request import Request
from sanic.response import HTTPResponse, json

from ..connections import get_client

node_bp = Blueprint('node')


@node_bp.route('/<node_id>/stats')
async def node_stats(request: Request, node_id: str) -> HTTPResponse:
    client = get_client(request)
    stats = (await client.nodes.stats(node_id=node_id))['nodes'][node_id]
    return json({
        'threadPool': stats['thread_pool']
    })


@node_bp.route('/<node_id>/info')
async def node_info(request: Request, node_id: str) -> HTTPResponse:
    client = get_client(request)
    info = (await client.nodes.info(node_id=node_id))['nodes'][node_id]
    return json({
        'OS': {
            "Ip Address": info['ip'],
            "Roles": ", ".join(info['roles']),
            "Logs Path": info['settings']['path']['logs'],
            "Home Path": info['settings']['path']['home'],
            "Available Processors": info['os']['available_processors'],
            "Allocated Processors": info['os']['allocated_processors']
        },
        "Thread Pools": {
            "search": "{x[queue_size]} / {x[size]}".format(x=info['thread_pool']['search']),
            "write": "{x[queue_size]} / {x[size]}".format(x=info['thread_pool']['write']),
            "get": "{x[queue_size]} / {x[size]}".format(x=info['thread_pool']['get']),
            "snapshot": "{x[queue_size]} / {x[max]}".format(x=info['thread_pool']['snapshot']),
            "management": "{x[queue_size]} / {x[max]}".format(x=info['thread_pool']['management']),
            "force_merge": "{x[queue_size]} / {x[size]}".format(x=info['thread_pool']['force_merge']),
        },
        "JVM": {
            "pid": info['jvm']['pid'],
            "version": info['jvm']['version'],
            "vmName": info['jvm']['vm_name'],
            "vmVendor": info['jvm']['vm_vendor'],
            "startTimeInMillis": info['jvm']['start_time_in_millis'],
            "heapMaxInMb": info['jvm']['mem']['heap_max_in_bytes']/1024/1024

        }
    })
