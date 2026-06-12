import os
import duckdb
from dotenv import load_dotenv

load_dotenv()

DUCKDB_PATH = os.getenv(
    "DUCKDB_PATH",
    "./data/warehouse/macrofinanzas.duckdb"
    )

def get_connection():
    conn = duckdb.connect(DUCKDB_PATH)
    return conn

if __name__ == "__main__":
    conn = get_connection()
    result = conn.execute(
        "SELECT 'DuckDB conectado correctamente' AS mensaje;"
    ).fetchdf()

    print(result)
    conn.close()

