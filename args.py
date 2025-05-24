


curl -X POST http://127.0.0.1:8090/api/v1/metalakes -H 'Content-Type: application/json' -d '{"name": "example-metalake"}'

curl.exe -X POST http://127.0.0.1:8090/api/metalakes -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" -d "{\"name\": \"example-metalake\", \"comment\": \"This is a new metalake\", \"properties\": {}}"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@catalog.json"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs/catalog/schemas/my_namespace/tables -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@table.json"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs/catalog/schemas -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@schema.json"
curl.exe -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" --data "@namespace.json"
curl -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" -d '{ "namespace": ["demo"], "properties": { "location": "s3://warehouse/demo" } }'
curl.exe -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" --data "@namespace.json"

helm install minio minio/minio --set rootUser=admin --set rootPassword=password --set service.type=ClusterIP


helm install gravitino gravitino/charts/gravitino --set service.type=NodePort --set minio.enabled=false


docker run -d --name iceberg-rest --network iceberg_net --network-alias iceberg-rest -p 8181:8181 -e CATALOG_WAREHOUSE=s3://warehouse/ -e CATALOG_IO__IMPL=org.apache.iceberg.aws.s3.S3FileIO -e CATALOG_S3_ENDPOINT=http://minio:9000 -e AWS_ACCESS_KEY_ID=admin -e AWS_SECRET_ACCESS_KEY=password apache/iceberg-rest-fixture:latest

kubectl exec deployment/iceberg-rest -- curl -u admin:password http://host.minikube.internal:9000/warehouse

kubectl exec -it iceberg-rest-596955f564-6pm8p -- printenv | Select-String AWS
kubectl logs iceberg-rest-7b8dbc988f-4sqs2