
DROP TABLE IF EXISTS core.fact_balance_mensual;

CREATE TABLE IF NOT EXISTS core.fact_tipo_cambio
(
    sk_tiempo INT,
    sk_moneda INT,
    tasa_compra DOUBLE,
    tasa_venta DOUBLE,
    tasa_promedio DOUBLE,
    spread DOUBLE
);

CREATE TABLE IF NOT EXISTS core.fact_balance_mensual
(
    sk_tiempo INT,
    sk_entidad INT,
    activos_totales DOUBLE,
    cartera_creditos DOUBLE,
    depositos DOUBLE,
    patrimonio DOUBLE,
    resultado_neto DOUBLE,
    depositos_me DOUBLE,
    cartera_me DOUBLE
);

