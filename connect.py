import time
from langchain import OpenAI
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.sql import text

def get_connection_string(db_type, user, password, host, port, database):
    if db_type.lower() == 'postgresql':
        return f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    elif db_type.lower() == 'mysql':
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    else:
        raise ValueError("Unsupported database type. Supported types are 'PostgreSQL' and 'MySQL'")

start_time = time.time()

llm = OpenAI(temperature=0)

db_type = "PostgreSQL"  # Change this to "MySQL" for a MySQL database
user = "postgres"
password = "root"
host = "localhost"
port = 5432
database = "test"

try:
    connection_string = get_connection_string(db_type, user, password, host, port, database)
    with create_engine(connection_string).connect() as conn:
        print(f"Connected to the {db_type} database.")
        
        include_tables=['employees']
        try:
            rows = conn.execute("SELECT COUNT(*) FROM employees").scalar()
            print(f"Counted {rows} rows from the employees table.")
            
        except Exception as e:
            print(f"Failed to include tables: {e}")

except Exception as e:
    print(f"Failed to connect to the {db_type} database: {e}")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Time elapsed: {elapsed_time:.2f} seconds")
