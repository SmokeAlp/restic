from DataLogicLair.Models.product_input_model import *


class Sugar(Product):
    def __init__(self, amount_for_good):
        super().__init__(id=10,name='sugar', cost_per_amount=70, unit_of_measurement='kg')
        # self.amount_in_sklad = None
        self.amount_for_good = amount_for_good

