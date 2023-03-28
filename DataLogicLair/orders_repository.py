from DataLogicLair.get_conection import *
from pyodbc import Error


class Order_repository:
    def __init__(self):
        self.__options = Options()

    # def create_order(self, order):
    #     try:
    #         cnc = get_connection()
    #         cursor = cnc.cursor()
    #         order = {
    #             "cust_name": "Chel_1",
    #             "good_name_1": "Capucino", "amount1": 1,
    #             "good_name_2": "Salad", "amount2": 2
    #          }
    #         cursor.execute(self.__options.get_all_customer)
    #         if order.get("cust_name")
    #     except Error as err:
    #         print(f'create_order_error: {err}')

    # def create_order(self, order):
    #     try:
    #         cnc = get_connection()
    #         cursor = cnc.cursor()
    #         cursor.execute(self.__options.get_pro)
    #         query = self.__options.create_order
    #         cursor.execute(query)
    #         cnc.commit()
    #         cursor.execute(self.__options.get_last_order_id)
    #         order_id = cursor.fetchval()
    #         query = self.__options.create_customers_orders + f" {order_id}, {order.customer_id}"
    #         cursor.execute(query)
    #         cnc.commit()
    #         cursor.execute(self.__options.get_good_id_by_name + f" {order.good_name}")
    #         good_id = cursor.fetchval()
    #         query = self.__options.create_goods_orders + f" {good_id}, {order_id}, {order.good_amount}"
    #         cursor.execute(query)
    #         cnc.commit()
    #         cursor.execute(self.__options.get_products_amount_and_id_by_order_id + f" {order_id}")
    #         products_id_and_amount = cursor.fetchall()
    #         for i in products_id_and_amount:
    #             cursor.execute(self.__options.get_product_amount + f" {i.product_id}")
    #             pr_am_in_stock = cursor.fetchval()
    #             cursor.execute(self.__options.get_product_name_by_id + f' {i.product_id}')
    #             pr_name = cursor.fetchval()
    #             if pr_am_in_stock < i.product_amount:
    #                 print(f'не хватает {pr_name}, нужно больше денег денег денег денег денег для {pr_name}')
    #                 return False
    #         for i in products_id_and_amount:
    #             print(i.product_id, i.product_amount)
    #             cursor.execute(self.__options.update_product_amount + f" {i.product_id}, -{i.product_amount}")
    #             cnc.commit()
    #         cursor.execute(self.__options.update_customer_summ_money + f" {order.customer_id}")
    #         cnc.commit()
    #         cnc.close()
    #         print('order have been added successfully, products_amount have been update successfuly, earned money have been update successfuly')
    #     except Error as err:
    #         print(f'create_order_error: {err}')

    def get_all_orders(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_orders
        cursor.execute(query)
        return cursor.fetchall()
