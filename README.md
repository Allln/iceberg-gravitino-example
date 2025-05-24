# Iceberg + Gravitino + Trino + MinIO Example

This repository demonstrates a working deployment of a simple data lake stack using:

* **Apache Iceberg** (table format)
* **Apache Gravitino** (REST catalog)
* **Trino** (SQL query engine)
* **MinIO** (S3-compatible object store)

---

## Components

| Component | Purpose                         | Access URL                                     |
| --------- | ------------------------------- | ---------------------------------------------- |
| MinIO     | Object store for Iceberg tables | [http://localhost:9001](http://localhost:9001) |
| Gravitino | REST catalog for Iceberg        | [http://localhost:8090](http://localhost:8090) |
| Trino     | SQL engine for querying Iceberg | [http://localhost:8080](http://localhost:8080) |

---

## Setup Instructions

### 1. Start MinIO + Trino with Docker Compose

```bash
docker-compose up -d
```

* MinIO Console: [http://localhost:9001](http://localhost:9001)
* Trino Web UI: [http://localhost:8080](http://localhost:8080)

### 2. Deploy Gravitino with Helm

```bash
minikube start
helm install gravitino gravitino/charts/gravitino
```

If it's already deployed, skip to the next step.

### 3. Port Forward Gravitino

```bash
kubectl port-forward service/gravitino 8090:8090
```
Keep this running in a separate terminal.

---

## Gravitino Setup

### 4. Install Python Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Run Setup Scripts

Create metalake dynamicaly or through Gravitino UI 
http://localhost:8090/ui/metalakes
or
curl.exe -X POST "http://127.0.0.1:8090/api/metalakes" -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@metalake.json"

```bash
python create_catalog.py
python create_schema.py
```
These will:

* Create a Catalog called `catalog`
* Create a Schema called `schema`


---

## Web Interfaces

* Trino UI: http://localhost:8080/ui/](http://localhost:8080/ui/
* Gravitino UI: http://localhost:8090/ui/metalakes
* MinIO Console: http://localhost:9001/buckets](http://localhost:9001/buckets

Login to MinIO with:

Psst!
* **Access Key**: `minioadmin`
* **Secret Key**: `minioadmin`

Create a bucket called `warehouse` in MinIO.

---

##  Run Queries via Trino

```bash
docker exec -it iceberg-gravitino-example-trino-1 trino
```

Then run:

```sql
SHOW CATALOGS;
SHOW SCHEMAS FROM iceberg;
CREATE TABLE iceberg.demo.test_table (id INT, name VARCHAR);
INSERT INTO iceberg.demo.test_table VALUES 
    (3, 'Charlie'),
    (4, 'Diana'),
    (5, 'Eve');
SELECT * FROM iceberg.demo.test_table WHERE id > 2;
SELECT COUNT(*) FROM iceberg.demo.test_table;
CREATE TABLE iceberg.demo.test_table_tmp AS 
SELECT id, 
       CASE WHEN name = 'Eve' THEN 'Evelyn' ELSE name END AS name 
FROM iceberg.demo.test_table;

DROP TABLE iceberg.demo.test_table;

ALTER TABLE iceberg.demo.test_table_tmp RENAME TO test_table;
ALTER TABLE iceberg.demo.test_table ADD COLUMN email VARCHAR;

```

---
