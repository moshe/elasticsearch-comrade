from sanic import Sanic
from sanic.response import json

from blueprints.alias import alias_bp
from blueprints.cluster import cluster_bp
from blueprints.index import index_bp
from blueprints.rest import rest_bp
from blueprints.snapshot import snapshot_bp
from blueprints.task import task_bp
from blueprints.views import views_bp
from connections import clients, get_client

app = Sanic()
# app.static('/', './static')
app.blueprint(index_bp, url_prefix='/api/v1/index')
app.blueprint(rest_bp, url_prefix='/api/v1/rest')
app.blueprint(cluster_bp, url_prefix='/api/v1/cluster')
app.blueprint(alias_bp, url_prefix='/api/v1/alias')
app.blueprint(task_bp, url_prefix='/api/v1/task')
app.blueprint(snapshot_bp, url_prefix='/api/v1/snapshot')
app.blueprint(views_bp, url_prefix='/api/v1/views')


@app.route('/api/v1/clients')
async def get_clients(request):
    result = []
    for cluster_name in clients():
        client = get_client(None, cluster_name)
        health = await client.cluster.health()
        result.append({"name": cluster_name,
                       "status": health['status']})
    return json(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
