SELECT
    sk_tiempo,
    sk_entidad,
    count(*) as total
from core.fact_balance_mensual
GROUP BY
    sk_tiempo,
    sk_entidad\
HAVING count(*)>1;