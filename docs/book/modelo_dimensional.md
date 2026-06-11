# Modelo Dimensional

## Procesos de negocio

1. Mercado cambiario
2. Balances bancarios mensuales

## Tablas de hechos

### fact_tipo_cambio
Grano: Una fila por fecha y moneda

Medidas:
- tasa_compra
- tasa_venta
- tasa_promedio
- spread

### fact_balance_mensual
Grano: Una fila por mes y entidad financiera
Medidas:
- activos_totales
- cartera_creditos
- depositos
- patrimonio
- resultado_neto
- depositos_me
- cartera_me

## Dimensiones
- dim_tiempo
- dim_moneda
- dim_entidad_financiera

--------------------------------------------------------------------
Tabla                    Tipo           Grano
--------------------------------------------------------------------
dim_tiempo             Dimension  Una fila por dia
dim_moneda             Dimension  Una fila por moneda
dim_entidad_financiera Dimension  Una fila por version de entidad
fact_tipo_cambio       Hecho      Una fila por fecha y moneda
fact_balance_mensual   Hecho      Una fila por mes y entidad
---------------------------------------------------------------------

# Indicadores derivados
A partir de este modelo construiremos indicadores como:
- Tipo de cambio promedio
- Spead cambiario
- ROA
- ROE
- Dolarizacion de depositos
- Dolarizacion de cartera
- Concentracion bancaria

## Formulas principales
- tasa_promedio = (tasa_compra + tasa_venta)/2
- spread = tasa_venta - tasa_compra
- ROA = resultado_neto / activos_totales
- ROE = resultado_neto / patrimonio
- dolarizacion_depositos = depositos_me / depositos
- dolarizacion_carte = cartera_me / cartera_creditos