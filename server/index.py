import traceback

from elasticsearch import ElasticsearchException
from sanic import Sanic
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, file, json
from ujson import dumps

from blueprints.alias import alias_bp
from blueprints.cluster import cluster_bp
from blueprints.index import index_bp
from blueprints.node import node_bp
from blueprints.rest import rest_bp
from blueprints.snapshot import snapshot_bp
from blueprints.task import task_bp
from blueprints.template import template_bp
from blueprints.views import views_bp
from connections import clients

app = Sanic()
app.static('/static', './static')
app.blueprint(views_bp, url_prefix='/api/v1/views')
app.blueprint(index_bp, url_prefix='/api/v1/index')
app.blueprint(rest_bp, url_prefix='/api/v1/rest')
app.blueprint(cluster_bp, url_prefix='/api/v1/cluster')
app.blueprint(alias_bp, url_prefix='/api/v1/alias')
app.blueprint(task_bp, url_prefix='/api/v1/task')
app.blueprint(snapshot_bp, url_prefix='/api/v1/snapshot')
app.blueprint(template_bp, url_prefix='/api/v1/template')
app.blueprint(node_bp, url_prefix='/api/v1/node')


@app.route('/')
async def redirect_init(request):
    return await file('static/index.html')


@app.route('/api/v1/clients')
async def get_clients(request: Request) -> HTTPResponse:
    result = []
    for cluster_name in clients():
        result.append({"name": cluster_name})
    return json(result)


@app.exception(Exception)
async def halt_response(request: Request, exception: Exception) -> HTTPResponse:
    if isinstance(exception, ElasticsearchException):
        error = {"error": exception.info, "type": "ElasticSearch error"}
    else:
        error = {"error": traceback.format_exc(), "type": "unexpected"}
    logger.error(dumps(error))
    return json(error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
