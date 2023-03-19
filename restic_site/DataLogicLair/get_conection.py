import pyodbc
from DataLogicLair.options import *
from pyodbc import Error


def get_connection():
    connection = None
    conString = Options()
    try:
        connection = pyodbc.connect(conString.connection_string)
        print("MySQL Database connection successful...")
    except Error as err:
        print(f"Error: '{err}'")
    return connection



