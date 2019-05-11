import re
import ujson
from sanic.response import json
from sanic import Blueprint

from connections import get_client

task_bp = Blueprint('task')

task_query_regex = re.compile('source\[(.*)\]')


@task_bp.route('/list')
async def list_tasks(request):
    result = []
    client = get_client()
    # S6 - ES6 does't support group_by=none
    tasks = await client.tasks.list(detailed=True)
    for node_id, node in tasks['nodes'].items():
        for task_id, task in node['tasks'].items():
            formatted = {
                "taskId": task_id,
                "action": task['action'],
                "running_time_in_ms": task["running_time_in_nanos"] / 1_000_000,
                "cancellable": task["cancellable"],
                "nodeName": node['name'],
            }
            if task['description']:
                formatted['description'] = task['description']
                query = task_query_regex.search(task['description'])
                if query is not None:
                    formatted['query'] = ujson.loads(query.groups()[0])
            result.append(formatted)
    return json(result)
