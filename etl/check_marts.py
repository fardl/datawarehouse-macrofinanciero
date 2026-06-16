from db import get_connection

conn=get_connection()

with open(
    "sql/check_marts.sql",
    'r',
    encoding='utf-8'
) as file:

    sql = file.read()

    result = conn.execute(sql).fetchdf()

    print(result)

conn.close()