import json
from collections import ChainMap
from glob import glob
from os import path

from elasticsearch_async import AsyncElasticsearch
from sanic.request import Request

clusters = {}
defaults = {"retry_on_timeout": True, "timeout": 30}


def load_clients(clusters_dir: str) -> None:
    connections_dir = path.abspath(path.join(path.dirname(path.abspath(__file__)), clusters_dir))
    for connection in glob(connections_dir + '/*'):
        if not connection.endswith('.json'):
            raise RuntimeError(f'Connections dir {connections_dir} requires json files')
        info = json.load(open(connection))
        if 'params' not in info:
            raise RuntimeError(f'Missing params key in {connection}')
        name = info.get('name')
        if name is None:
            name = connection.split('/')[-1].replace('.json', '')
        info['client'] = AsyncElasticsearch(**ChainMap(info['params'], defaults))
        clusters[name] = info


def get_client(request: Request, cluster: str = None) -> AsyncElasticsearch:
    cluster_name = cluster or request.headers['x-elastic-cluster']
    return clusters[cluster_name]['client']
