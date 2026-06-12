from db import get_connection

conn = get_connection()

with open(
    'sql/04_load_dimensions.sql',
    'r',
    encoding='utf-8'
) as file:
    sql=file.read()
    conn.execute(sql)
    conn.close()

print('Dimensiones cargadas')