SELECT
'tipo_cambio_raw' AS tabla,
COUNT(*) AS total_filas
FROM staging.tipo_cambio_raw

UNION ALL

SELECT
'balance_bancario_raw' AS tabla,
COUNT(*) AS total_filas
FROM staging.balance_bancario_raw;