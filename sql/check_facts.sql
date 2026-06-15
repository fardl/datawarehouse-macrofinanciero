SELECT
    'fact_tipo_cambio' as tabla,
    count(*) as total_filas
from core.fact_tipo_cambio

union ALL
select
    'fact_balance_mensual' as tabla,
    count(*) as total_filas
from core.fact_balance_mensual;
