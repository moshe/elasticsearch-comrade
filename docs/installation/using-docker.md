---
description: Docker is the most recommended way to run Comrade in production.
---

# Using Docker

Images are hosted in DockerHub and tagged in every version.

In order to pull and run run the following command

```bash
docker run -v $PWD/clusters/:/app/clusters/ -it -p 8000:8000 mosheza/elasticsearch-comrade
```

For more information regarding the **clusters** directory and Comrade's varius configuration option please refer the [Configuration](https://moshe-1.gitbook.io/comrade/configuration/) section

