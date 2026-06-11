from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DB = os.getenv("DB_NAME")
USER = os.getenv("DB_USER") 
PASSWORD = os.getenv("DB_PASSWORD")

connection_string = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
engine = create_engine(connection_string)   

print("Database connection established successfully.")



from sqlalchemy import text

with engine.connect() as connection:
    resultado = connection.execute(text("SELECT version();"))
    

for fila in resultado:
    print(fila)
