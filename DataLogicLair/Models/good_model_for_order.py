import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options


class Good_for_order:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.__options = Options()
        self.cnc = get_connection()
        self.__cursor = self.cnc.cursor()
        self.products_for_this_good = []

    def get_good_id_by_name(self):
        self.__cursor.execute(self.__options.get_good_id_by_name + f" {self.name}")
        return self.__cursor.fetchval()

    def get_needed_products_amount_and_id_for_good_by_good_id(self):
        self.__cursor.execute(self.__options.get_needed_products_amount_and_id_for_good_by_good_id + f" {self.get_good_id_by_name()}")
        return self.__cursor.fetchall()