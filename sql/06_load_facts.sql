delete from core.fact_tipo_cambio;
delete from core.fact_balance_mensual;

INSERT INTO core.fact_tipo_cambio
(
    sk_tiempo,
    sk_moneda, 
    tasa_compra,
    tasa_venta,
    tasa_promedio,
    spread
)
SELECT
    t.sk_tiempo,
    m.sk_moneda,
    CAST(r.tasa_compra AS DOUBLE)
        AS tasa_compra,
    CAST(r.tasa_venta AS DOUBLE)
        AS tasa_venta,
    (
        CAST(r.tasa_compra AS DOUBLE)
        +
        CAST(r.tasa_venta AS DOUBLE)

    )/2
        AS tasa_promedio,
    (
    
        CAST(r.tasa_venta AS DOUBLE)
        -
        CAST(r.tasa_compra AS DOUBLE)
    ) 
        AS spread

FROM staging.tipo_cambio_raw r

JOIN core.dim_tiempo t
ON t.fecha = 
    STRPTIME(
    r.fecha,
    '%Y-%m-%d'
    )

JOIN core.dim_moneda m
ON m.moneda_cod = r.moneda

WHERE r.fecha IS NOT NULL
AND r.moneda IS NOT NULL
AND CAST(r.tasa_compra AS DOUBLE) >0
AND CAST(r.tasa_venta as DOUBLE)>0;


INSERT INTO core.fact_balance_mensual
(
    sk_tiempo,
    sk_entidad,
    activos_totales,
    cartera_creditos,
    depositos,
    patrimonio,
    resultado_neto,
    depositos_me,
    cartera_me
)

SELECT
    t.sk_tiempo,
    e.sk_entidad,
    cast(r.activos_totales as double)
    as activos_totales,

    cast(r.cartera_creditos as double)
    as cartera_creditos,

    cast(r.depositos as double)
    as depositos,

    cast(r.patrimonio as double)
    as patrimonio,

    cast(r.resultado_neto as double)
    as resultado_neto,

    cast(r.depositos_me as double)
    as depositos_me,

    cast(r.cartera_me as double)
    as cartera_me

FROM staging.balance_bancario_raw r
JOIN core.dim_tiempo t
    ON t.fecha =
        last_day(
            strptime(
                r.periodo,
                '%Y-%m-%d'
            )::DATE
        )
JOIN core.dim_entidad_financiera e
ON e.entidad_cod = r.entidad_cod

WHERE r.periodo IS NOT NULL
AND r.entidad_cod IS NOT NULL;
   