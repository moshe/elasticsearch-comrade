#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import json
import sys

from elasticsearch_async import AsyncElasticsearch

lines = open('../esopen/data/47').readlines()

found = []


async def test(ip):
    s = None
    try:
        client = AsyncElasticsearch(hosts=[ip])
        # s = await client.cluster.health()
        s = await client.cluster.stats()
        found.append({'ip': ip, 'versions': s['nodes']['versions'], 'stats': s})
    except Exception:
        pass
    if s:
        print(ip)


async def main():
    tasks = []
    for line in sys.stdin:
        tasks.append(test(json.loads(line)['ip']))
    await asyncio.gather(*tasks)
    json.dump(found, open('/tmp/found.json', 'w'))

asyncio.run(main())
