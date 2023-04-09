import pyodbc

from pyodbc import Error

from DataLogicLair.options import Options


def get_connection():
    connection = None
    conString = Options()
    try:
        connection = pyodbc.connect(conString.connection_string)
    except Error as err:
        print(f"Error: '{err}'")
    return connection
