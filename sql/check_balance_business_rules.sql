SELECT *
FROM core.fact_balance_mensual
WHERE depositos_me > depositos;

SELECT *
FROM core.fact_balance_mensual
WHERE cartera_me > cartera_creditos;

