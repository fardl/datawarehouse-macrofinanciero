from db import get_connection

def run_sql(path, conn):
    with open(path, "r", encoding="utf-8") as file:
        sql = file.read()
    conn.execute(sql)
    

def main():
    conn = get_connection()
    run_sql("sql/01_create_schemas.sql", conn)
    run_sql("sql/02_staging_ddl.sql", conn)
    conn.close()

print("Base DuckDB inicializada correctamente.")

if __name__ == "__main__":
    main()