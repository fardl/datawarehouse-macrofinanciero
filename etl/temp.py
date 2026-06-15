from db import get_connection

def run_query(sql_file):

    conn = get_connection()

    with open(
        sql_file,
        "r",
        encoding="utf-8"
    ) as file:

        sql = file.read()

    result = conn.execute(
        sql
    ).fetchdf()

    conn.close()

    return result

print(
    run_query(
        "sql/05_facts_ddl.sql"
    )
)