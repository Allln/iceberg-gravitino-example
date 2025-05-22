import gravitino

from gravitino.client.gravitino_client import GravitinoClient
from gravitino import Catalog

client = GravitinoClient(uri="http://localhost:8090", metalake_name="metalake")
catalog = client.create_catalog(
    name="catalog",
    catalog_type=Catalog.Type.FILESET,
    provider="hadoop",
    comment="This is a Hadoop fileset catalog",
    properties={"location": "file:///tmp/root"}
)
print(f"Catalog created: {catalog}")
