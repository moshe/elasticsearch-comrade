---
description: Mostly for development purpose
---

# From Source

{% hint style="warning" %}
 This guide assumes your computer is suited with:  
node &gt;= 12 , python &gt;= 3.7 and pipenv
{% endhint %}

```bash
# Clone the repo
git clone git@github.com:moshe/elasticsearch-comrade.git

# Install server deps
cd elasticsearch-comrade
pipenv install -e . --skip-lock

# Install client deps
cd client
npm install
```

Now you should open two terminals, one for running the server and the second for serving the client

### Starting the server

```bash
pipenv run python index.py  # In the root of the project 
```

### Starting the client

```bash
cd client
npm run serve
```

