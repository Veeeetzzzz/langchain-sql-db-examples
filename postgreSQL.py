import time
from langchain import OpenAI
from langchain.sql_database import SQLDatabase
from sqlalchemy import create_engine
from sqlalchemy.sql import text

start_time = time.time()

llm = OpenAI(temperature=0)

user = "postgres"
password = "root"
host = "localhost"
port = 5432
database = "test"

try:
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
    print("Connected to the database.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")

include_tables=['employees']

try:
    db = SQLDatabase(engine, include_tables=include_tables)
    print(f"Included tables: {', '.join(include_tables)}")
except Exception as e:
    print(f"Failed to include tables: {e}")

row_count_query = text("SELECT COUNT(*) FROM employees")
row_count = engine.execute(row_count_query).scalar()
print(f"Counted {row_count} rows from the employees table.")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time elapsed: {elapsed_time:.2f} seconds")
