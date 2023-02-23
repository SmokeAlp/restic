from DataLogicLair.get_conection import *
from mysql.connector import Error


class Product_repository:
    def __init__(self):
        self.__options = Options()

    def create_product(self, product):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_product + f" '{product.name}', {product.amount}, {product.cost_per_amount}, {product.unit_of_measurement}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('product have been added successfully')
        except Error as err:
            print(f'create_products_error: {err}')

    def get_all_products(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_products
        cursor.execute(query)
        return cursor.fetchall()
