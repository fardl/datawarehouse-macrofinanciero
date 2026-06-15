SELECT
    t.fecha,
    e.entidad_cod,
    e.entidad_nombre,
    f.activos_totales,
    f.depositos,
    f.patrimonio,
    f.resultado_neto

FROM core.fact_balance_mensual f
JOIN core.dim_tiempo t
ON t.sk_tiempo = f.sk_tiempo
JOIN core.dim_entidad_financiera e
ON e.sk_entiedad = f.sk_entidad
ORDER BY
    t.fecha,
    e.entiedad_cod
LIMIT 10;