from db import get_connection

conn = get_connection()

result = conn.execute(
"""
SELECT
    anio_mes,
    COUNT(*)
FROM mart.vw_hhi_bancario
GROUP BY anio_mes
ORDER BY anio_mes;
"""
).fetchdf()

print(result)

conn.close()