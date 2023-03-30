
from pyodbc import Error

from restic_site.DataLogicLair.get_conection import get_connection
from restic_site.DataLogicLair.options import Options


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
            print('product have been created successfully')
        except Error as err:
            print(f'create_products_error: {err}')
 
    def add_product(self, product_name, amount):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            product_id = cursor.execute(self.__options.get_product_id_by_name + f" {product_name}")
            query = self.__options.update_product_amount + f" {product_id.fetchval()}, {amount}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('product have been added successfully')
        except Error as err:
            print(f'create_products_error: {err}')

    def check_summ_of_money_for_product_amount(self, product_name, amount):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.get_product_id_by_name + f" {product_name}"
            product_id = cursor.execute(query)
            cursor.execute(self.__options.check_summ_of_money_for_product_amount + f" {product_id.fetchval()}, {amount}")
            return str(cursor.fetchval()) + ' рублей'
        except Error as err:
            print(f'create_products_error: {err}')

    def get_all_products(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_products
        cursor.execute(query)
        return cursor.fetchall()
