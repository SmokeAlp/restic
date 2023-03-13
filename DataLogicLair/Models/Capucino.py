from DataLogicLair.Models.good_model_for_order import *
from DataLogicLair.Models.Prodcuts_models.milk import *
from DataLogicLair.Models.Prodcuts_models.sugar import *
from DataLogicLair.Models.Prodcuts_models.cream import *
from DataLogicLair.Models.Prodcuts_models.coffee_beans import *


class Capucino(Good_for_order):

    def __init__(self, amount):
        super().__init__(name='Capucino', amount=amount)
        self.milk = Milk(1)
        self.cream = Cream(1)
        self.sugar = Sugar(1)
        self.coffe_beans = Coffe_Beans(1)
        self.products_for_this_good = [self.milk, self.cream, self.sugar, self.coffe_beans]

