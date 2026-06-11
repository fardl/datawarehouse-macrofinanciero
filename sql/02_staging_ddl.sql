CREATE TABLE IF NOT EXISTS 
staging.tipo_cambio_raw 
(
    fecha TEXT,
    moneda TEXT,
    tasa_compra TEXT,
    archivo_origen TEXT,
    
    cargado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS
staging.balance_bancario_raw
(
    periodo TEXT,
    entidad_cod TEXT,
    entidad_nombre TEXT,
    tipo_entidad TEXT,
    activos_totales TEXT,
    cartera_creditos TEXT,
    depositos TEXT,
    patrimonio TEXT,
    resultado_neto TEXT,
    depositos_me TEXT,
    cartera_me TEXT,
    archivo_origen TEXT,
        
    cargado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    
);