import json
from collections import ChainMap
from glob import glob

from elasticsearch_async import AsyncElasticsearch
from sanic.request import Request

clusters = {}
defaults = {"retry_on_timeout": True, "timeout": 30}


def load_clients(clusters_dir: str) -> None:
    for connection in glob(clusters_dir + '/*'):
        if not connection.endswith('.json'):
            raise RuntimeError(f'Connections dir {clusters_dir} requires json files')
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
