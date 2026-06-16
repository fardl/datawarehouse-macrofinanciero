import pandas as pd

fx = pd.read_csv("data/raw/tipo_cambio.csv")
balances = pd.read_csv("data/raw/balances.csv")

print("\nTipo_de_Cambio")
print(fx.head())

print("\nBalances")
print(balances.head())


# Numero de filas y columnas
print(fx.info())
print(balances.info())

# Validaciones basicas
print(fx.isnull().sum())
print(balances.isnull().sum())

# Procesar datos
fx["fecha"] = pd.to_datetime(fx["fecha"])
fx["tasa_compra"] = fx["tasa_compra"].astype(float)
fx["tasa_venta"] = fx["tasa_venta"].astype(float)
balances['periodo'] = pd.to_datetime(balances['periodo'])

# Guardar datos procesados
fx.to_csv("data/processed/tipo_cambio.csv", index=False)
balances.to_csv("data/processed/balances.csv", index=False)
