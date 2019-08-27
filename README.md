# Elasticsearch Comrade [![CircleCI](https://circleci.com/gh/moshe/elasticsearch-comrade.svg?style=svg)](https://circleci.com/gh/moshe/elasticsearch-comrade)
Elasticsearch Comrade is an open-source Elasticsearch admin and monitoring panel highly inspired by Cerebro.
Elasticsearch Comrade built with python3, VueJS, Sanic and Vuetify2
![Alt text](/docs/screenshots/main_dark.png?raw=true "Optional Title")

# Main Features
- Elasticsearch version 5,6 and 7 support
- Built for big clusters
- Node statistics and monitoring
- Manage aliases
- Inspect running tasks
- Rest API with autocompletion, history, templates, and history
- Manage index templates
- Manage snapshots
- Multi cluster support
- And more ...


# Docs
soon

# Installation
The recommended way to run Comrade in production is using the docker container  
`docker run -p8000:8000 -it moshe/elasticsearch-comrade`

# Discovery
TODO

# Development
- Clone the repo
- cd client && npm install && npm run serve
- cd server && pipenv install && pipenv run python index.py
