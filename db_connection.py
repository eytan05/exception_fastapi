import psycopg2
from dotenv import load_dotenv
import os
from psycopg2 import OperationalError


def get_env_var():
    load_dotenv(".env")
    return {
        "username": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
    }


def connect_to_db():
    try:
        env_vars = get_env_var()
        connection = psycopg2.connect(
            dbname=env_vars["database"],
            user=env_vars["username"],
            password=env_vars["password"],
            host=env_vars["host"],
            port=env_vars["port"],
        )
        return connection
    except OperationalError as e:
        print(
            f"L'erreur '{e}' s'est produite. La base de données n'est pas accessible."
        )
