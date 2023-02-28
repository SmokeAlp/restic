from DataLogicLair.get_conection import *
from mysql.connector import Error
from DataLogicLair.goods_orders_repository import *


class Order_repository:
    def __init__(self):
        self.__options = Options()
        self.__create_goods_orders = Goods_orders_repository()

    def create_order(self, customer_name, position, good_name, amount):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.check_availability_of_customer + f" {position}"
            if cursor.execute(query).fetchval() == 1:
                good_id = cursor.execute(self.__options.get_good_id_by_name + f" '{good_name}'")
                cursor.execute(self.__options.create_goods_orders + f" {good_id.fetchval()}, {order_id}, {amount}")
                cnc.commit()
                cursor.execute(self.__options.update_order_price_by_id + f" {order_id}")
                cnc.commit()
                products_id_and_amount = cursor.execute(self.__options.get_products_amount_and_id_by_order_id + f" {order_id}")
                for i in products_id_and_amount.fetchall():
                    print(i.product_id, i.product_amount)
                    cursor.execute(self.__options.update_product_amount + f" {i.product_id}, -{i.product_amount}")
                    cnc.commit()
            elif cursor.execute(query).fetchval() == 0:
                cursor.execute(self.__options.create_order + f" '{customer_name}', {amount}, {0}")
                # good_id = cursor.execute(self.__options.get_good_id_by_name + f" {good_name}")
                # cursor.execute(self.__options.create_goods_orders + f" {good_id.fetchval()}, {order_id}, {amount}")
                cnc.commit()
                res = cursor.execute(self.__options.get_all_orders).fetchall()
                for i in res:
                    print(i)
                self.__create_goods_orders.create_goods_orders(good_name, order_id, amount)
                cnc.commit()
                cursor.execute(self.__options.update_order_price_by_id + f" {order_id}")
                cnc.commit()
                product_id_and_amount = cursor.execute(self.__options.get_products_amount_and_id_by_order_id + f" {order_id}")
                for i in products_id_and_amount.fetchall():
                    print(i.product_id, i.product_amount)
                    cursor.execute(self.__options.update_product_amount + f" {i.product_id}, -{i.product_amount}")
                    cnc.commit()
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
