from db import get_connection

conn = get_connection()

result = conn.execute(
"""
DESCRIBE staging.tipo_cambio_raw;
"""
).fetchdf()

print(result)

conn.close()