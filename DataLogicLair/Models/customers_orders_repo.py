from DataLogicLair.get_conection import *
from pyodbc import Error


class Customers_orders_repository:

    def __init__(self):
        self.__options = Options()

    def create_goods_orders(self, customer_name, order_id):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            cursor.execute(self.__options.get_cu)
            query = self.__options.create_goods_orders + f" {}, {order_id}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('create_goods_orders completed successfully')
        except Error as err:
            print(f'create_goods_orders_error: {err}')

