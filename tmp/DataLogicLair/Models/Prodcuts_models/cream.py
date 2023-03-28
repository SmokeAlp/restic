from DataLogicLair.Models.product_input_model import *



class Cream(Product):
    def __init__(self, amount_for_good):
        super().__init__(id=11,name='cream', cost_per_amount=750, unit_of_measurement='kg')
        # self.amount_in_sklad = None
        self.amount_for_good = amount_for_good


