import gravitino

from gravitino.client.gravitino_client import GravitinoClient
from gravitino import Catalog

client = GravitinoClient(uri="http://localhost:8090", metalake_name="metalake")
catalog = client.list_catalogs()
print(catalog)
catalog = client.load_catalog(name = catalog[0])
schema = catalog.as_schemas().create_schema(
    schema_name="schema",
    comment="This is a schema",
    properties={"location": "file:///tmp/root/schema"}
)
print(f"Schema created: {schema}")