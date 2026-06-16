import duckdb
import pandas as pd

# Definir ruta de DuckDB
DB_PATH = "data/warehouse/macrofinanzas.duckdb"


# Crear funcion de consulta
# Esta funcion permite consultar DuckDB desde Streamlit 
# y devolver los resultados como un Dataframe de Pandas 
def run_query(query):
    conn = duckdb.connect(DB_PATH)
    df = conn.execute(
        query
    ).fetchdf()
    conn.close()
    return df

# Configurar la pagina

# Cargando los datos desde  mart
resumen = run_query(
    """
        SELECT *
        FROM mart.vw_resumen_macrofinanciero
        ORDER BY anio_mes
    """
)

fx = run_query(
    """
        SELECT *
        FROM mart.vw_tipo_cambio_diario
        ORDER BY fecha
    """
)

banca = run_query(
    """
        SELECT *
        FROM mart.vw_indicadores_banca
        ORDER BY fecha
    """
)

hhi = run_query(
    """
        SELECT *
        FROM mart.vw_hhi_bancario
        ORDER BY anio_mes
    """
)


# Creat KPIs principales
ultimo = resumen.sort_values(
    'anio_mes'
).tail(1)

if not ultimo.empty:
    tasa_promedio = ultimo[
        "tasa_promedio_mes"
    ].iloc[0]
                           
    activos = ultimo[
        "activos_totales_sistema"
    ].iloc[0]

    depositos = ultimo[
        "depositos_sistema"
    ].iloc[0]

    dolarizacion = ultimo[
        "dolarizacion_depositos_sistema"
    ].iloc[0]

    entidades =banca[
    "entidad_nombre"
].dropna().unique()

