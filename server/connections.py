from elasticsearch_async import AsyncElasticsearch

cached_client = None


def get_client():
    global cached_client
    if cached_client is None:
        cached_client = AsyncElasticsearch(hosts=['http://222.85.141.99'])
    return cached_client
