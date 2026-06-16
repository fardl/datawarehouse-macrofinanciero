CREATE OR REPLACE VIEW mart.vw_tipo_cambio_diario as
select 
    t.fecha,
    t.anio,
    t.mes,
    t.anio_mes,
    m.moneda_mes,
    m.moneda_nombre,
    f.tasa_compra,
    f.tasa_venta,
    f.tasa_promedio,
    f.spread

from core.fact_tipo_cambio f
join core.dim_tiempo t
on t.sk_tiempo  = f.sk_tiempo

join core.dim_moneda m
on m.sk_moneda = f.sk_moneda;

CREATE OR REPLACE VIEW mart.vw_indicadores_banca AS
SELECT
    t.fecha,
    t.anio,
    t.mes,
    t.anio_mes,
    e.entidad_cod,
    e.entidad_nombre,
    e.tipo_entidad,
    f.activos_totales,
    f.cartera_creditos,
    f.depositos,
    f.patrimonio,
    f.resultado_neto,
    f.depositos_me,
    f.cartera_me,
    f.resultado_neto
        /NULLIF(f.activos_totales,0)
        AS roa,
    f.resultado_neto
        /NULLIF(f.patrimonio, 0)
        AS roe,
    f.cartera_me
        /NULLIF(f.cartera_creditos,0)
        AS dolarizacion_cartera
FROM core.fact_balance_mensual f
JOIN core.dim_tiempo t
ON t.sk_tiempo = f.sk_tiempo

JOIN core.dim_entiedad_financiera e
ON e.sk_entidad = f.sk_entidad;

CREATE OR REPLACE VIEW mart.vw_hhi_bancario AS
WITH cuotas AS
    (
        SELECT
            t.fecha,
            t.anio_mes,
            e.entidad_cod,
            e.entidad_nombres,
            f.activos_totales,
            f.activos_totales
                /NULLIF(
                    SUM(f.activos_totales)
                    OVER (
                        PARTITION BY t.anio_mes
                    ),
                    0
                )
                AS cuotas_activos
        FROM core.fact_balance_mensual f
        JOIN core.dim_tiempo t
            ON t.sk_tiempo = f.sk_tiempo
        JOIN core.dim_entidad_financiera e
            ON e.sk_entidad = f.sk_entidad
    )
SELECT
    fecha,
    anio_mes,
    SUM(
        POWER(cuota_activos,2)
    ) AS hhi_activos
FROM cuotas
GROUP BY
    fecha,
    anio_mes
ORDER BY
    anio_mes;

CREATE OR REPLACE VIEW mart.vw_resumen_macrofinanciero AS
WITH fx AS
    (
        SELECT
            anio_mes,
            AVG(tasa_promedio)
                AS tasa_promedio_mes,
            AVG(spread)
                AS spead_promedio_mes
        FROM mart.vw_tipo_cambio_diario
        WHERE moneda_cod = 'USD'
        GROUP BY
            anio_mes
    ),
    banca AS
    (
        SELECT
            anio_mes,
            SUM(activos_totales)
                AS activos_totales_sistema,
            SUM(depositos)
                AS depositos_sistema,
            SUM(resultado_neto)
                AS resultado_neto_sistema,
            SUM(depositos_me)
                / NULLIF(SUM(depositos),0)
                AS dolarizacion_depositos_sistema
        FROM mart.vw_indicadores_banca
        GROUP BY
            anio_mes
    )

    SELECT
        b.anio_mes,
        fx.tasa_promedio_mes,
        fx.spread_promedio_mes, 
        b.activos_totales_sistema,
        b.depositos_sistema,
        b.resultado_neto_sistema,
        b.dolarizacion_depositos_sistema
    FROM banca b
    LEFT JOIN fx
    ON fx.anio_mes = b.anio_mes
    ORDER BY
        b.anio_mes;
