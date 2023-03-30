from DataLogicLair.get_conection import *
from DataLogicLair.options import *
from pyodbc import Error


class Customer_repository:
    def __init__(self):
        self.__options = Options()

    def create_customer(self, customer):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_customer + f" {customer.name}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('create_customer completed successfully')
        except Error as err:
            print(f'create_customer_error: {err}')

    def get_all_customer(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_customer
        cursor.execute(query)
        return cursor.fetchall()
