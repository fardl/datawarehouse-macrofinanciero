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
    conn = get_connection()
    run_sql_file(
        "sql/07_marts.sql",
        conn
    )

    conn.close()

print(
    "Marts creados correctamente."
)


if __name__ == "__main__":
    main()
