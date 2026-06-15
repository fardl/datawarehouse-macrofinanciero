SELECT
    sk_tiempo,
    sk_moneda,
    count(*) as total
FROM core.fact_tipo_cambio
GROUP BY
    sk_tiempo,
    sk_moneda
HAVING count(*) >1;