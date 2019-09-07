---
description: Project setup and tests
---

# Development

## Tech stack

### Backend

* python 3.7
* [Sanic](https://github.com/huge-success/sanic) - Async Python 3.6+ web server/framework \| Build fast. Run fast.
* [uvloop](https://github.com/MagicStack/uvloop) - Ultra fast asyncio event loop.
* [elasticsearch-py-async](https://github.com/elastic/elasticsearch-py-async) - Backend for elasticsearch-py based on python's asyncio module.

### Frontend

* [Vue.js](https://vuejs.org/) - The Progressive JavaScript Framework
* [Vuetify](https://vuetifyjs.com/) - Material Design Component Framework
* [Cypress](https://www.cypress.io/) - Fast, easy and reliable testing for anything that runs in a browser. Install _Cypress_ in seconds and take the pain out of front-end testing.

## Setting up

Please follow the [installation guide from source](installation/from-source.md)

## Running Tests

### Server tests

```text
py.test server
```

### End to end \(cypress\)

```text
cd e2e
npx cypress run
```

## Linters

### flake8

```text
cd server
pipenv run flake8 --ignore=E501
```

### eslint

```text
cd client
npm run lint
```

