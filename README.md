# 🧳 Iceberg + Gravitino + Trino + MinIO Example

This repository demonstrates a working deployment of a simple data lake stack using:

* **Apache Iceberg** (table format)
* **Apache Gravitino** (REST catalog)
* **Trino** (SQL query engine)
* **MinIO** (S3-compatible object store)

---

## ✨ Components

| Component | Purpose                         | Access URL                                     |
| --------- | ------------------------------- | ---------------------------------------------- |
| MinIO     | Object store for Iceberg tables | [http://localhost:9001](http://localhost:9001) |
| Gravitino | REST catalog for Iceberg        | [http://localhost:8090](http://localhost:8090) |
| Trino     | SQL engine for querying Iceberg | [http://localhost:8080](http://localhost:8080) |

---

## ✅ Setup Instructions

### 1. Start MinIO + Trino with Docker Compose

```bash
docker-compose up -d
```

* MinIO Console: [http://localhost:9001](http://localhost:9001)
* Trino Web UI: [http://localhost:8080](http://localhost:8080)

### 2. Deploy Gravitino with Helm

```bash
minikube start
helm install gravitino charts/gravitino
```

If it's already deployed, skip to the next step.

### 3. Port Forward Gravitino

```bash
kubectl port-forward service/gravitino 8090:8090
```

Keep this running in a separate terminal.

---

## 📝 Gravitino Setup

### 4. Install Python Dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 5. Run Setup Scripts

Create metalake dynamicaly or through Gravitino UI 
http://localhost:8090/ui/metalakes
```bash
python create_catalog.py
python create_schema.py
```
These will:

* Create a Catalog called `catalog`
* Create a Schema called `schema`


---

## 📃 Web Interfaces

* Trino UI: http://localhost:8080/ui/](http://localhost:8080/ui/
* Gravitino UI: http://localhost:8090/ui/metalakes
* MinIO Console: http://localhost:9001/buckets](http://localhost:9001/buckets

Login to MinIO with:

Psst!
* **Access Key**: `minioadmin`
* **Secret Key**: `minioadmin`

Create a bucket called `warehouse` in MinIO.

---

## ⚙️ Run Queries via Trino

```bash
docker exec -it iceberg-gravitino-example-trino-1 trino --catalog catalog --schema schema
```

Then run:

```sql
SHOW TABLES;
CREATE TABLE my_table (id INT, name VARCHAR);
INSERT INTO my_table VALUES (1, 'Alice'), (2, 'Bob');
SELECT * FROM my_table;
```

---

## ♻️ Restarting Everything After Reboot

1. Start Docker stack:

```bash
docker-compose up -d
```

2. Start port forwarding:

```bash
kubectl port-forward service/gravitino 8090:8090
```

3. (Optional) Rerun setup scripts if necessary:

```bash
python create_catalog.py
python create_schema.py
```

4. Visit UIs:

* [Trino](http://localhost:8080/ui/)
* [Gravitino](http://localhost:8090/ui/metalakes?metalake=metalake&catalog=catalog&type=fileset&schema=schema)
* [MinIO](http://localhost:9001/buckets)

---

