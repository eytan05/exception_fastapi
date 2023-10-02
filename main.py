from fastapi import FastAPI, HTTPException, status

from db_connection import connect_to_db
from db_search import get_customers_info, CustomerNotFoundError, DatabaseConnectionError
from db_setup import setup_database

app = FastAPI()


@app.get("/")
async def read_root():
    connection = connect_to_db()
    setup_database(connection)
    return {"message": "Hello, welcome to the API!"}


@app.get("/customer/{name}")
async def read_customer(name: str):
    try:
        connection = connect_to_db()
        customers_info = get_customers_info(name,connection)
        return {"customers": customers_info}
    except CustomerNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Customers not found"
        )
    except DatabaseConnectionError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal issue occurred, please contact the team in charge of the API"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unknown error occurred"
        )






