import pyodbc
from mysql.connector import *
from DataLogicLair.options import *


def get_connection():
    connection = None
    conString = Options()
    try:
        connection = pyodbc.connect(conString.connection_string)
        print("MySQL Database connection successful...")
    except Error as err:
        print(f"Error: '{err}'")
    return connection



