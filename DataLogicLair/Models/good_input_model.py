import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options

def get_needed_products_amount_and_id_for_good_by_good_id(goods_id):
    opt = Options()
    cnc = get_connection()
    cursor = cnc.cursor()
    cursor.execute(
        opt.get_needed_products_amount_and_id_for_good_by_good_id + f" {goods_id}")
    return cursor.fetchall()

def max_value_good_amount(good_id):
    l = list(map(lambda x: x[2]//x[1], get_needed_products_amount_and_id_for_good_by_good_id(good_id)))
    return min(l)


class Good:
    def __init__(self, name=str, cost=int, products=dict):
        self.name = name
        self.cost = cost
        self.products = products
        self.__options = Options()
        self.cnc = get_connection()
        self.__cursor = self.cnc.cursor()

    def get_good_id_by_name(self):
        print(self.name)
        self.__cursor.execute(self.__options.get_good_id_by_name + f" '{self.name}'")
        return self.__cursor.fetchval()

    def get_needed_products_amount_and_id_for_good_by_good_id(self):
        self.__cursor.execute(
            self.__options.get_needed_products_amount_and_id_for_good_by_good_id + f" {self.get_good_id_by_name()}")
        return self.__cursor.fetchall()

    def __str__(self):
        return self.name
