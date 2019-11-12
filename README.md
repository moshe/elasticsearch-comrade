# Elasticsearch Comrade ![python](https://img.shields.io/badge/python-v3.7-blue.svg) [![docker pulls](https://img.shields.io/docker/pulls/mosheza/elasticsearch-comrade.svg)](https://hub.docker.com/r/mosheza/elasticsearch-comrade 'DockerHub') [![CircleCI](https://circleci.com/gh/moshe/elasticsearch-comrade.svg?style=svg)](https://circleci.com/gh/moshe/elasticsearch-comrade) [![GitHub issues](https://img.shields.io/github/issues/moshe/elasticsearch-comrade)](https://github.com/moshe/elasticsearch-comrade/issues) [![GitHub license](https://img.shields.io/github/license/moshe/elasticsearch-comrade)](https://github.com/moshe/elasticsearch-comrade/blob/master/LICENSE) 
Elasticsearch Comrade is an open-source Elasticsearch admin and monitoring panel highly inspired by Cerebro.
Elasticsearch Comrade built with python3, VueJS, Sanic, Vuetify2 and Cypress
![Alt text](/docs/.gitbook/assets/image%20(16).png?raw=true "Optional Title")
![Alt text](https://moshe.sh/.netlify/functions/img?source=github "Optional Title")
# Main Features
- Elasticsearch version 5,6 and 7 support (tested against elasticsearch 7.4)
- Multi cluster
- Rest API with autocompletion, history, templates, and history
- SQL editor (version 7 only)
- Built for big clusters
- Node statistics and monitoring
- Manage aliases
- Inspect running tasks
- Manage index templates
- Manage snapshots
- And much more ...

# Quckstart
### Cluster dir definitaions
Comrade discovers clusters using the `--clusters-dir` param, docs are [here](https://moshe-1.gitbook.io/comrade/configuration/cluster-discovery), examples are [here](https://github.com/moshe/elasticsearch-comrade/tree/master/server/tests)
### Using docker (recommended)
`docker run -v $PWD/clusters/:/app/clusters/ -it -p 8000:8000 mosheza/elasticsearch-comrade`
### Using the python package
`pip install elasticsearch-comrade`  
`comrade --clusters-dir clusters`

# Installation, configuration and next steps
[Here](https://moshe-1.gitbook.io/comrade/)

# [Roadmap](https://github.com/moshe/elasticsearch-comrade/milestones?state=open)
### [v1.1.0](https://github.com/moshe/elasticsearch-comrade/milestone/2)
- [X] Add python package
- [ ] Reindex screen
- [ ] Comrade dashboard
### [v1.2.0](https://github.com/moshe/elasticsearch-comrade/milestone/4)
- Cluster settings screen
- Evacuate node from shards
- Add commrade version indicator to footer
### v1.3.0
- Beats screen
- Threadpools screen

# Screenshots
![Alt text](/docs/.gitbook/assets/image%20(2).png?raw=true "Optional Title")
![Alt text](/docs/.gitbook/assets/image%20(5).png?raw=true "Optional Title")
![Alt text](/docs/.gitbook/assets/image%20(9).png?raw=true "Optional Title")
![Alt text](/docs/.gitbook/assets/image%20(7).png?raw=true "Optional Title")
![Alt text](/docs/.gitbook/assets/image%20(8).png?raw=true "Optional Title")
