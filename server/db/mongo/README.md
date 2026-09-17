# Local MongoDB server

This Docker Compose project runs MongoDB locally for the data-wrangling notebook. It has no username or password because the lesson uses an unauthenticated connection. Port `27017` is bound to `127.0.0.1`, so MongoDB is not exposed to other machines on the network.

## Prerequisites

- Docker Desktop is installed and running.
- Project dependencies have been installed with `uv sync`.

## Start MongoDB

From the repository root, run:

```powershell
docker compose -f server/db/mongo/docker-compose.yml up -d
```

Wait until the container is healthy:

```powershell
docker compose -f server/db/mongo/docker-compose.yml ps
```

Test MongoDB directly:

```powershell
docker compose -f server/db/mongo/docker-compose.yml exec mongodb mongosh --quiet --eval "db.adminCommand('ping')"
```

## Load the Nairobi data

Open `notebooks/data-science-lab/8_Data_Wrangling_with_MongoDB/Project.ipynb`, select the project's `.venv` kernel, and run:

```python
from pymongo import MongoClient
from load_mongo_data import load_nairobi_to_mongodb

host = "localhost"
port = 27017

load_nairobi_to_mongodb(host=host)

client = MongoClient(f"mongodb://{host}:{port}")
client.admin.command("ping")
```

The loader recreates `air-quality.nairobi` and imports `nairobi.parquet`.

## View logs

```powershell
docker compose -f server/db/mongo/docker-compose.yml logs -f mongodb
```

## Stop or reset MongoDB

Stop MongoDB while retaining its data:

```powershell
docker compose -f server/db/mongo/docker-compose.yml down
```

Delete MongoDB and its persistent volume:

```powershell
docker compose -f server/db/mongo/docker-compose.yml down --volumes
```

The reset command permanently deletes the locally stored MongoDB data.
