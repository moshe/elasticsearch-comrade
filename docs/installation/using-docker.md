---
description: Docker is the most recommended way to run Comrade in production.
---

# Using Docker

Images are hosted in DockerHub and tagged in every version.

In order to pull and run run the following command

```bash
docker run -v clusters/:clusters/ -it -p 8000:8000 moshe/elasticsearch-comrade
```

For more information regarding configuring Comrade please refer the Configuration section

