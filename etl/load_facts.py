from db import get_connection

def run_sql_file(path, conn):
    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        sql = file.read()

    conn.execute(sql)

def main():
    conn=get_connection()

    run_sql_file(
        "sql/05_facts_ddl.sql",
        conn
    )


    run_sql_file(
        "sql/06_load_facts.sql",
        conn
    )

    conn.close()

print("Hechos cargados correctamente")

if __name__ == "__main__":
    main()