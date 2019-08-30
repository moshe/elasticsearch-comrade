---
description: Cluster discovery explained
---

# Cluster Discovery

The discovery system behind Comrade is pretty simple.  
During startup the service lists the content of **clusters** folder and load all the files that ends with .json.  
Each json have the connection information for a single cluster. Comrade uses the [official python client of elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/) and the **params** key passed directly to Elasticsearch connection constructor.

### Examples

#### Http plain connection

```javascript
{
    "name": "clustername",
    "params": {
        "hosts": ["http://3.219.233.212:9200"]
    }
}
```

#### SSL and auth

```javascript
{
    "params":  {
        "hosts": ["localhost", "otherhost"],
        "http_auth": ["user", "secret"],
        "scheme": "https",
        "port": 443
    }
}
```

More examples [here](https://elasticsearch-py.readthedocs.io/en/master/#ssl-and-authentication)

