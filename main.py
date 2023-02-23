from DataLogicLair.product_repository import *
from DataLogicLair.Models.product_input_model import *

product = Product_repository()
product_model = Product('cake', 1200, 45, 'штука')
product.add_products(product_model)

res = product.get_all_products()

for i in res:
    print(i)





