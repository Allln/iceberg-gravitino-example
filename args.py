


curl -X POST http://127.0.0.1:8090/api/v1/metalakes -H 'Content-Type: application/json' -d '{"name": "example-metalake"}'

curl.exe -X POST http://127.0.0.1:8090/api/metalakes -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" -d "{\"name\": \"example-metalake\", \"comment\": \"This is a new metalake\", \"properties\": {}}"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@catalog.json"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs/catalog/schemas/my_namespace/tables -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@table.json"

curl.exe -X POST http://127.0.0.1:8090/api/metalakes/metalake/catalogs/catalog/schemas -H "Accept: application/vnd.gravitino.v1+json" -H "Content-Type: application/json" --data "@schema.json"
curl.exe -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" --data "@namespace.json"
curl -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" -d '{ "namespace": ["demo"], "properties": { "location": "s3://warehouse/demo" } }'
curl.exe -X POST http://localhost:8181/v1/namespaces -H "Content-Type: application/json" --data "@namespace.json"
