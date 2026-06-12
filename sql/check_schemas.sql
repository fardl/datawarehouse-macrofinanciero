SELECT schema_name
FROM information_schema.schemata
WHERE schema_name IN 
(
    'staging',
    'core',
    'mart'
)
ORDER BY schema_name;


