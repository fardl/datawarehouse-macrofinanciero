import duckdb
import pandas as pd
import streamlit as st
import plotly.express as px

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
st.set_page_config(
    page_title = "Dashboard Macrofinanciero RD",
    page_icon = " ",
    layout = "wide"
)

st.title(
    "Dashboard Macrofinanciero RD"
)

st.caption(
    "Proyecto de Data Warehouse macrofinanciero con DuckDB y Streamlit"
)


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

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "tipo de cambio promedio",
        round(tasa_promedio,2)
    )

    col2.metric(
        "Activos del sistema",
        f"{activos:,.0f}"
    )

    col3.metric(
        "Depositos del sistema",
        f"{depositos:,.0f}"
    )

    col4.metric(
        "Dolarizacion depositos",
        f"{dolarizacion:.2%}"
    )

    # Grafico de tipo de cambio
    st.subheader(
        "Evolucion del tipo de cambio"
    )

    fig_fx = px.line(
        fx,
        x="fecha",
        y="tasa_promedio",
        title="Tipo de cambio promedio diario"
    )

    st.plotly_chart(
        fig_fx,
        use_container_width=True
    )

# Graficos de indicadores bancarios

st.subheader(
    "Indicadores bancarios"
)

entidades =banca[
    "entidad_nombre"
].dropna().unique()

entidad_seleccionada=st.selectbox(
    "Seleccione una entidad financiera",
    entidades
)

banca_filtrada = banca[
    banca["entidad_nombre"] 
    ==
    entidad_seleccionada
]

fig_roa = px.line(
    banca_filtrada,
    x="fecha",
    y='roa',
    title="ROA"
)

st.plotly_chart(
    fig_roa,
    use_container_width=True
)


fig_roe = px.line(
    banca_filtrada,
    x="fecha",
    y='roe',
    title="ROE"
)

st.plotly_chart(
    fig_roe,
    use_container_width=True
)


# Grafico dolarizacion
st.subheader("Dolarizacion bancaria")

df_dolarizacion = banca_filtrada[
    [
        "fecha",
        "dolarizacion_depositos",
        "dolarizacion_cartera"
    ]
].copy()

df_dolarizacion = df_dolarizacion.melt(
    id_vars="fecha",
    value_vars=[
        "dolarizacion_depositos",
        "dolarizacion_cartera"
    ],
    var_name="indicador",
    value_name="dolarizacion"
)

fig_dolarizacion = px.line(
    df_dolarizacion,
    x="fecha",
    y="dolarizacion",
    color="indicador",
    title="Dolarizacion de depositos y cartera"
)

st.plotly_chart(
    fig_dolarizacion,
    use_container_width=True
)


# Grafico de concentracion bancaria
st.subheader("Concentracion bancaria")

fig_hhi = px.line(
    hhi,
    x="anio_mes",
    y="hhi_activos",
    title="Indice HHI por activos"
)

st.plotly_chart(
    fig_hhi,
    use_container_width=True
)

# Mostrar tablas de datos
with st.expander(
    "Ver resumen macrofinanciero"
):
    st.dataframe(
        resumen,
        use_container_width=True
    )

with st.expander(
    "Ver indicadores bancarios"
):
    st.dataframe(
        banca,
        use_container_width=True
    )















































