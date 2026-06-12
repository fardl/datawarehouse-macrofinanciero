from db import get_connection

def run_sql_file(path):
    conn = get_connection()

    with open(path, "r", encoding="utf-8") as file:
        sql = file.read()

    result = conn.execute(sql).fetchdf()

    print(result)

    conn.close()

if __name__ == "__main__":
    run_sql_file("sql/monitor_staging.sql")

print("Script SQL ejecutado correctamente.")