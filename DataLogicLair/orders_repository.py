from DataLogicLair.get_conection import *
from pyodbc import Error


class Order_repository:
    def __init__(self):
        self.__options = Options()

    def create_order(self, order):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_order
            cursor.execute(query)
            cnc.commit()
            cursor.execute(self.__options.get_last_order_id)
            order_id = cursor.fetchval()
            query = self.__options.create_customers_orders + f" {order_id}, {order.customer_id}"
            cursor.execute(query)
            cnc.commit()
            cursor.execute(self.__options.get_good_id_by_name + f" {order.good_name}")
            good_id = cursor.fetchval()
            query = self.__options.create_goods_orders + f" {good_id}, {order_id}, {order.good_amount}"
            cursor.execute(query)
            cnc.commit()
            cursor.execute(self.__options.get_products_amount_and_id_by_order_id + f" {order_id}")
            products_id_and_amount = cursor.fetchall()
            for i in products_id_and_amount:
                print(i.product_id, i.product_amount)
                cursor.execute(self.__options.update_product_amount + f" {i.product_id}, -{i.product_amount}")
                cnc.commit()
            cursor.execute(self.__options.update_customer_summ_money + f" {order.customer_id}")
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
