CREATE OR REPLACE VIEW mart.vw_tipo_cambio_diario as
select 
    t.fecha,
    t.anio,
    t.mes,
    t.anio_mes,
    m.moneda_mes,
    m.moneda_nombre,
    f.tasa_compra,
    f.tasa_venta