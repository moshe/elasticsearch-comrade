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
cd elasticsearch-comrade/server
pipenv install

# Install client deps
cd ../client
npm install
```

Now you should open two terminals, one for running the server and the second for serving the client

### Starting the server

```bash
cd server
pipenv run python index.py
```

### Starting the client

```bash
cd client
npm run serv
```

