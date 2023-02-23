from DataLogicLair.products_repository import *
from DataLogicLair.goods_repository import *
from DataLogicLair.Models.product_input_model import *
from DataLogicLair.Models.good_input_model import *
from DataLogicLair.Models.order_input_model import *
from DataLogicLair.orders_repository import *
from DataLogicLair.goods_products_repository import *



#CREATE AND GET PRODUCT
# product = Product_repository()
# product_model = Product('cake', 1200, 45, 'shtuka')
# product.create_product(product_model)
#
# res = product.get_all_products()
#
# for i in res:
#     print(i)

#CREATE AND GET GOOD
# good = Goods_repository()
# good_model = Good('Capucino', 125)
# good.create_good(good_model)
#
# res = good.get_all_goods()
#
# for i in res:
#     print(i)

#CREATE AND GET ORDER
# order = Order_repository()
# # order_model = Order('Chel', 450, 3)
# # order.create_order(order_model)
#
# res = order.get_all_orders()
#
# for i in res:
#     if i.customer_name == 'Chel':
#         r = i.customer_name
#         print(r)


#1 METHOD HOW TO CREATE AND GET GOODS_PRODUCTS
# good_product = Goods_products_repository()
# good_product.create_goods_products('coffee beans', 'Capucino', 1)
#
# res_g_p = good_product.get_all_goods_products()
#
# for i in res_g_p:
#     print(i)


# product = 'milk'
# good = 'Capucino'
# opt = Options()
# cnc = get_connection()
# cursor = cnc.cursor()
# product_id_and_good_id = cursor.execute(opt.get_product_id_and_good_id_by_name + f" {product}, {good}")
# k = [i for i in product_id_and_good_id]
# q = k[0]
# print(q[0])

#2 METHOD HOW TO CREATE AND GET GOODS_PRODUCTS
# good_product = Goods_products_repository()
# good_product.create_goods_products('cream', 'Capucino', 1)
#
# res_g_p = good_product.get_all_goods_products()
#
# for i in res_g_p:
#     print(i)
