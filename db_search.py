import logging
from psycopg2 import OperationalError, sql

logging.basicConfig(level=logging.INFO)


class DatabaseConnectionError(Exception):
    pass

class CustomerNotFoundError(Exception):
    pass

# database.py

def get_customers_info(name: str,connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT firstname, lastname, age FROM customer WHERE firstname = %s OR lastname = %s", (name, name))
        results = cursor.fetchall()
        if not results:
            raise CustomerNotFoundError(f"No customers found with name: {name}")
        customers_info = [{"name": f"{result[0]} {result[1]}", "age": result[2]} for result in results]
        return customers_info
    except OperationalError as e:
        logging.error(f"Database connection error: {e}")
        raise DatabaseConnectionError("Database connection error")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise

