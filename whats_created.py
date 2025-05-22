import gravitino

from gravitino.client.gravitino_client import GravitinoClient
from gravitino import Catalog

client = GravitinoClient(uri="http://localhost:8090", metalake_name="metalake")
catalog = client.list_catalogs()
print(catalog)
catalog = client.load_catalog(name = catalog[0])

schemas = catalog.as_schemas().list_schemas()
for s in schemas:
    print(f"Schema: {s}")