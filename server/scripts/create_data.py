#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from elasticsearch import Elasticsearch, helpers

client = Elasticsearch()

INDICES_TO_CREATE = ['empty', 'git']

for index in INDICES_TO_CREATE:
    if client.indices.exists(index):
        client.indices.delete(index)
    client.indices.create(index)

gitlog = os.popen('''git log --pretty=format:'{"sha": "%H", "author_name": "%aN", "author_email": "%aE", "date": "%ad", "message": "%f"}' ''').readlines()
bulk = []
for line in gitlog:
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})
    bulk.append({'_index': 'git', '_source': json.loads(line)})

helpers.bulk(client, bulk)
