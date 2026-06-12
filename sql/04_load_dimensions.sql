DELETE FROM core.dim_entidad_financiera;
DELETE FROM core.dim_moneda;
DELETE FROM core.dim_tiempo;

INSERT INTO core.dim_tiempo
SELECT
    CAST(strftime(fecha, '%Y%m%d') AS INTEGER) AS sk_tiempo,
    fecha,
    year(fecha) AS anio,
    month(fecha) AS mes,
    quarter(fecha) AS trimestre,
    CAST(strftime(fecha, '%Y%m') AS INTEGER) AS anio_mes,
    monthname(fecha) AS nombre_mes,
    fecha = last_day(fecha) AS es_fin_de_mes
FROM generate_series(
    DATE '2022-01-01',
    DATE '2024-12-31',
    INTERVAL 1 DAY
) t(fecha);

INSERT INTO core.dim_moneda
SELECT
    ROW_NUMBER() OVER (ORDER BY moneda) AS sk_moneda,
    moneda AS moneda_cod,
    CASE
        WHEN moneda = 'USD' THEN 'Dolar Estados Unidos'
        WHEN moneda = 'EUR' THEN 'Euro'
        ELSE moneda
    END AS moneda_nombre
FROM (
    SELECT DISTINCT moneda
    FROM staging.tipo_cambio_raw
) x;

INSERT INTO core.dim_entidad_financiera
SELECT
    ROW_NUMBER() OVER (ORDER BY entidad_cod) AS sk_entidad,
    entidad_cod,
    entidad_nombre,
    tipo_entidad,
    DATE '2022-01-01' AS vigente_desde,
    DATE '9999-12-31' AS vigente_hasta,
    TRUE AS es_actual
FROM (
    SELECT DISTINCT
        entidad_cod,
        entidad_nombre,
        tipo_entidad
    FROM staging.balance_bancario_raw
) x;