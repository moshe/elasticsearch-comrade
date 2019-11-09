import concurrent
import traceback
from os import path

import click
from elasticsearch import ElasticsearchException
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.log import logger
from sanic.request import Request
from sanic.response import HTTPResponse, file, json

from .blueprints.alias import alias_bp
from .blueprints.cluster import cluster_bp
from .blueprints.index import index_bp
from .blueprints.node import node_bp
from .blueprints.rest import rest_bp
from .blueprints.snapshot import snapshot_bp
from .blueprints.task import task_bp
from .blueprints.template import template_bp
from .blueprints.views import views_bp
from .connections import clusters, load_clients

app = Sanic()
current_dir = path.dirname(__file__)
app.static('/static', f'{current_dir}/static')
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
    print(f'{current_dir}/static/index.html')
    return await file(f'{current_dir}/static/index.html')


@app.route('/api/v1/clients')
async def get_clients(request: Request) -> HTTPResponse:
    result = []
    for cluster_name in clusters:
        result.append({"name": cluster_name})
    return json(result)


@app.exception(Exception)
async def halt_response(request: Request, exception: Exception) -> HTTPResponse:
    if isinstance(exception, ElasticsearchException):
        error = {"error": exception.info, "type": "ElasticSearch error"}
        if isinstance(exception.args[2], concurrent.futures._base.TimeoutError):
            error['error'] = 'timeout'

    elif isinstance(exception, NotFound):
        return await file('static/index.html')
    else:
        error = {"error": traceback.format_exc(), "type": "unexpected"}
    logger.exception(exception)
    return json(error)


@app.listener('after_server_start')
async def notify_server_started(app, loop):
    load_clients(app.config.clusters_dir)


@app.listener('before_server_stop')
async def close_db(app, loop):
    for cluster in clusters:
        await clusters[cluster]['client'].transport.close()


@click.command()
@click.option('--port', default=8000, help='Specify port number', show_default=True)
@click.option('--host', default='0.0.0.0', help='Specify ip to bind', show_default=True)
@click.option('--debug', default=False, help='Run server in debug', is_flag=True, show_default=True)
@click.option('--cert', help='Path to your cert file', type=click.Path(exists=True))
@click.option('--key', help='Path to your key file', type=click.Path(exists=True))
@click.option('--clusters-dir',
              help='Path to your clusters dir',
              type=click.Path(exists=True),
              default=path.abspath(path.join(path.dirname(path.abspath(__file__)), 'clusters')),
              show_default=True)
def cli(port: int, host: str, debug: bool, cert: str, key: str, clusters_dir: str):
    app.config.clusters_dir = clusters_dir
    ssl = None
    if key and not cert:
        raise click.UsageError('--key supplied without --cert')
    elif cert and not key:
        raise click.UsageError('--cert supplied without --key')
    elif cert and key:
        ssl = {'cert': cert, 'key': key}
    app.run(host=host, port=port, debug=debug, ssl=ssl)


def main():
    cli(auto_envvar_prefix='COMRADE')


if __name__ == '__main__':
    main()
