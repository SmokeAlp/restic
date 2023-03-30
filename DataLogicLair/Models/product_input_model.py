from DataLogicLair.get_conection import *
from DataLogicLair.options import *


class Product:
    def __init__(self, id, name, cost_per_amount, unit_of_measurement):
        self.id = id
        self.name = name
        self.cost_per_amount = cost_per_amount
        self.unit_of_measurement = unit_of_measurement
        self.cnc = get_connection()
        self.__cursor = self.cnc.cursor()
        self.__options = Options()


    @property
    def amount_in_sklad(self):
        self.__cursor.execute(self.__options.get_product_amount_by_id + f" {self.id}")
        return self.__cursor.fetchval()
    @amount_in_sklad.setter
    def amount_in_sklad(self, value=int):
        self._amount_in_sklad = value