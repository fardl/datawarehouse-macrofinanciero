from db import get_connection

def run_sql_file(path, conn):
    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        sql = file.read()
        conn.execute()
    
