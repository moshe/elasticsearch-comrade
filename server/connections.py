from elasticsearch_async import AsyncElasticsearch
from sanic.request import Request

cache = {}


def get_client(request: Request, cluster: str = None) -> AsyncElasticsearch:
    global cache
    cluster_name = cluster or request.headers['x-elastic-cluster']
    if cluster_name not in cache:
        # cache = AsyncElasticsearch(hosts=['http://222.85.141.99'])  # default one
        # cache = AsyncElasticsearch(hosts=['http://58.209.250.114'])
        # cache = AsyncElasticsearch(hosts=['http://211.148.18.253'])
        cache[cluster_name] = AsyncElasticsearch(**clients()[cluster_name])  # backups
    return cache[cluster_name]


def clients() -> dict:
    return {
        "my-cluster": {
            "hosts": ['http://222.85.141.99']
        },
        "backups": {
            "hosts": ['http://52.213.100.155']
        },
        "vidmoon-master1": {
            "hosts": ['http://172.106.164.147']
        },
        "elasticsearch": {
            "hosts": ['http://13.76.247.223']
        },
        "huadong": {
            "hosts": ['http://211.148.18.253']
        },
        "azure": {
            "hosts": ['http://35.200.194.186']
        },
        "multiplefs": {
            "hosts": ['http://162.144.40.30']
        },
        "s3": {
            "hosts": ['http://13.250.14.119']
        },
        "701": {
            "hosts": ['http://209.208.59.202']
        },
        "720": {
            "hosts": ['http://192.3.162.113']
        }
    }
