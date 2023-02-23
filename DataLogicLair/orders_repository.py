from DataLogicLair.get_conection import *
from mysql.connector import Error


class Order_repository:
    def __init__(self):
        self.__options = Options()

    def create_order(self, order):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_order + f" '{order.customer_name}', {order.position}, {order.price} "
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('order have been added successfully')
        except Error as err:
            print(f'create_order_error: {err}')

    def get_all_orders(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_orders
        cursor.execute(query)
        return cursor.fetchall()
