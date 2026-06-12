CREATE TABLE IF NOT EXISTS core.dim_tiempo
(
    sk_tiempo INTEGER PRIMARY KEY,
    fecha DATE NOT NULL,
    anio INTEGER,
    mes INTEGER,
    trimestre INTEGER,
    anio_mes INTEGER,
    nombre_mes VARCHAR,
    es_fin_de_mes BOOLEAN
);

CREATE TABLE IF NOT EXISTS core.dim_moneda
(
    sk_moneda INTEGER PRIMARY KEY,
    moneda_cod VARCHAR,
    moneda_nombre VARCHAR
);

CREATE TABLE IF NOT EXISTS core.dim_entidad_financiera
(
    sk_entidad INT PRIMARY KEY,
    entidad_cod VARCHAR,
    entidad_nombre VARCHAR,
    tipo_entidad VARCHAR,
    vigente_desde DATE,
    vigente_hasta DATE,
    es_actual BOOLEAN
);