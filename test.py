import timeit
from pyodbc import Error
from DataLogicLair.goods_repository import *
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options
from DataLogicLair.orders_repository import Order_repository

code_to_test = """
from pyodbc import Error
from DataLogicLair.goods_repository import Goods_repository
from DataLogicLair.Models.good_model_for_order import get_needed_products_amount_and_id_for_good_by_good_id
from DataLogicLair.canAddProductToCart import ordersInCart
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options

db_goods = Goods_repository()
def get_all_goods(self):
    cnc = get_connection()
    cursor = cnc.cursor()
    query = self.__options.get_all_goods
    cursor.execute(query)
    goods = cursor.fetchall()
    needProducts = {}
    for good in ordersInCart:
        for product in good.get_needed_products_amount_and_id_for_good_by_good_id():
            if product.id not in needProducts.keys():
                needProducts[product.id] = product.product_amount * good.amount
            else:
                needProducts[product.id] += product.product_amount * good.amount
    goodsR = []
    for good in goods:
        ok = True
        for product in get_needed_products_amount_and_id_for_good_by_good_id(good.id):
            ok = ok and (product.product_amount + needProducts[product.id]) <= product.amount
        goodsR.append([good, ok])
    return goodsR
db_goods.get_all_goods()
"""

elapsed_time =  timeit.timeit(code_to_test, number=1)/100
print(elapsed_time)



options = Options()
cnc = get_connection()
cursor = cnc.cursor()
print(get_needed_products_amount_and_id_for_good_by_good_id(8))


order = Order_repository()

for i in order.get_all_orders():
    print(type(i.isDel))

    