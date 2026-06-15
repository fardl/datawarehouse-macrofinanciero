SELECT 
    'dim_tiempo' AS tabla,
    count(*) as total_filas
FROM core.dim_tiempo

UNION ALL

SELECT
    'dim_moneda' as tabla,
    COUNT(*)
FROM core.dim_moneda

UNION ALL

SELECT
    'dim_entidad_financiera' as tabla,
    COUNT(*)
FROM core.dim_entidad_financiera
;