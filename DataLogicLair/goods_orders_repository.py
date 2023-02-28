from DataLogicLair.options import *
from DataLogicLair.get_conection import *
from pyodbc import Error

class Goods_orders_repository:

    def __init__(self):
        self.__options = Options()

    def create_goods_orders(self, good_name, order_id, amount):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            good_id = cursor.execute(self.__options.get_good_id_by_name + f" {good_name}")
            query = self.__options.create_goods_orders + f" {good_id.fetchval()}, {order_id}, {amount} "
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('create_goods_orders completed successfully')
        except Error as err:
            print(f'create_goods_orders_error: {err}')

