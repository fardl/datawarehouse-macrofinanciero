from db import get_connection

conn = get_connection()

result=conn.execute(
    open(
        "sql/monitor_staging.sql"
    ).read()
).fetchdf()

print(result)