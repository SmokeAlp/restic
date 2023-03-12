from DataLogicLair.get_conection import *
from DataLogicLair.options import *
class Good_for_order:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.__options = Options()
        self.cnc = get_connection()
        self.__cursor = self.cnc.cursor()

    def get_good_id_by_name(self):
        self.__cursor.execute(self.__options.get_good_id_by_name + f" {self.name}")
        return self.__cursor.fetchval()

    def get_needed_products_amount_and_id_for_good_by_good_id(self):
        self.__cursor.execute(self.__options.get_needed_products_amount_and_id_for_good_by_good_id + f" {self.get_good_id_by_name()}")
        return self.__cursor.fetchall()