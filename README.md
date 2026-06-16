# Data Warehouse Macrofinanciero RD

Proyecto practco para construir una plataforma 

## Objetivo
Construir un flujo completo de datos que permita:
* Ingerir datos desde archivos CSV.
* Almacenarlos en DuckDB.
* Organizar la informacion en capas staging, core y mart.
* Construir indicadores macrofinancieros.
* Publicar un dashboard interactivo en Streamlit

## Arquitectura
CSV -> Python -> DyckDB  -> Staging -> Core -> Mart -> Streamlit

## Tecnologias
* Python
* DuckDB
* Pandas
* Streamlit
* Plotly
* Git
* GitHub

## Estructura del proyecto
app/
data/
docs/
etl/
sql/
test/

## Como ejecutar el proyecto
1. Crear entorno virtual
python -m venv .venv

2. Activar entorno virtual
.venv\Scripts\activate

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar pipeline
python etl/run_pipeline.py

5. Abrir dashboard
streamlit run app/streamlit_app.py

## Author
Francisco A. Ramirez