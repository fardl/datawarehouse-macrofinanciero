import pandas as pd
from db import get_connection
from datetime import datetime

fx = pd.read_csv('./data/raw/tipo_cambio.csv')
print(
    f"Filas FX: {len(fx)}"
)

balances = pd.read_csv('./data/raw/balances.csv')
print(
    f"Filas Balances: {len(balances)}"
)

# Agregar metadatos
fx['archivo_origen'] = ('tipo_cambio.csv')
balances['archivo_origen'] = ('balances.csv')

# Agregar timestamp:
fx['cargado_en'] =( datetime.now())
balances['cargado_en'] = (datetime.now())

# Cargar a DuckDB
conn = get_connection()

# Limpiar tablas staging
conn.execute("DELETE FROM staging.tipo_cambio_raw;")
conn.execute("DELETE FROM staging.balance_bancario_raw;")


# Registrar DataFrames
conn.register('fx_df', fx)
conn.register('balances_df', balances)

# Cargar tipo de cambio
conn.execute(
"""
    INSERT INTO
             staging.tipo_cambio_raw
    SELECT *
    FROM fx_df;
    
"""
)

# Cargar balances
conn.execute(
"""
    INSERT INTO
             staging.balance_bancario_raw
    SELECT *
    FROM balances_df;
    
"""
)

# Verificar conteos
result_fx = conn.execute(
"""
SELECT COUNT(*)
FROM staging.tipo_cambio_raw;
"""
).fetchone()[0]

result_balances = conn.execute(
"""
SELECT COUNT(*)
FROM staging.balance_bancario_raw;
"""
).fetchone()[0]

print(f"Filas en staging FX: {result_fx}")
print(f"Filas en staging balances: {result_balances}")

# Cerrar conexión
conn.close()

print("Carga a staging completada exitosamente.")