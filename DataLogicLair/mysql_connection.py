import mysql.connector
import pyodbc
from mysql.connector import *
from restic.DataLogicLair.`


def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect()
        print("MySQL Database connection successful...")
    except Error as err:
        print(f"Error: '{err}'")
    return connection



