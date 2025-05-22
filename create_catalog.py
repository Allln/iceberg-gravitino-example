import requests
import json

metalake = "demo"  # Replace with your metalake name
url = f"http://localhost:8090/api/metalakes/{metalake}/catalogs"

catalog_data = {
    "name": "iceberg_catalog",
    "type": "FILESYSTEM",
    "comment": "Iceberg catalog using MinIO as object store",
    "properties": {
        "warehouse": "s3a://warehouse",
        "s3.endpoint": "http://localhost:9000",
        "s3.access-key": "minioadmin",
        "s3.secret-key": "minioadmin"
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(catalog_data))

print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except Exception:
    print("Response Text:", response.text)
