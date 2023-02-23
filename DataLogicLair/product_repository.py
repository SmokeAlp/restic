from options import *
from mysql_connection import *


class Product_repository:
    def __init__(self):
        self.__options = Options()

    def add_products(self, product):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.add_products + f" '{product.name}', {product.amount}, {product.cost_per_amount}, {product.unit_of_measurement}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('product have been added successfully')
        except:
            print('add_products_error: check values, bro')

    def get_all_products(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_products
        cursor.execute(query)
        return cursor.fetchall()
