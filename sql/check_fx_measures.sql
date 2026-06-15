SELECT
    tasa_compra,
    tasa_venta,
    tasa_promedio,
    spread,
    (tasa_compra + tasa_venta)/2
    as tasa_promedio_recalculada,
    tasa_venta - tasa_compara
    as spread_recalculado

FROM core.fact_tipo_cambio
LIMIT 10;