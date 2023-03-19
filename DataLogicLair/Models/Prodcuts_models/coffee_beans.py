from DataLogicLair.Models.product_input_model import *


class Coffe_Beans(Product):
    def __init__(self, amount_for_good):
        super().__init__(id=9,name='coffe beans', cost_per_amount=1200, unit_of_measurement='kg')
        # self.amount_in_sklad = None
        self.amount_for_good = amount_for_good


