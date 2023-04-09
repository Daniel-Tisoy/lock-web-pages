from db import DbQueries
from os import getenv
from dotenv import load_dotenv
from sqlite3 import OperationalError

load_dotenv()
# load db configuration
db_name = getenv("DB_NAME")
db_table = getenv("DB_MAIN_TABLE_NAME")
db_column = getenv("DB_MAIN_COLUMN_NAME")
db_id_column = getenv("DB_ID_COLUMN_NAME")

if __name__ == "__main__":
    db_manager = DbQueries(db_name, db_table, db_column, db_id_column)
    try:
        db_manager.create_table()
        print("db table created succesfully")
    except OperationalError:
        print(f"db table {db_table} already exists")
