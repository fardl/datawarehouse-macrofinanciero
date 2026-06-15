SELECT
    t.fecha,
    m.moneda_cod,
    f.tasa_compra,
    f.tasa_venta,
    f.tasa_promedio,
    f.spread
FROM core.fact_tipo_cambio f
JOIN core.dim_tiempo t
ON t.sk_tiempo = f.sk_tiempo
JOIN core.dim_moneda m
ON m.sk_moneda = f.sk_moneda
ORDER BY
    t.fecha,
    m.moneda_cod
LIMIT 10;