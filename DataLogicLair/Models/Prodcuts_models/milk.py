from DataLogicLair.Models.product_input_model import *



class Milk(Product):
    def __init__(self, amount_for_good):
        super().__init__(id=8,name='milk', cost_per_amount=75, unit_of_measurement='l')
        # self.amount_in_sklad = None
        self.amount_for_good = amount_for_good


