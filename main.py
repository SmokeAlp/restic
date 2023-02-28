from DataLogicLair.products_repository import *
from DataLogicLair.goods_repository import *
from DataLogicLair.orders_repository import *
from DataLogicLair.goods_products_repository import *
from DataLogicLair.Models.product_input_model import *
from DataLogicLair.Models.good_input_model import *
from DataLogicLair.Models.order_input_model import *



#CREATE AND GET AND ADD PRODUCT
# product = Product_repository()
# product_model = Product('cake', 1200, 45, 'shtuka')
# product.create_product(product_model)
#
# product.add_product('Apple', 10)
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


#CREATE AND GET GOODS_PRODUCTS
# good_product = Goods_products_repository()
# good_product.create_goods_products('coffee beans', 'Capucino', 1)
#
# res_g_p = good_product.get_all_goods_products()
#
# for i in res_g_p:
#     print(i)


# opt = Options()
# cnc = get_connection()
# cursor = cnc.cursor()
# product = 'coffee beans'
# good = 'Capucino'
# product_id_and_good_id_by_name = cursor.execute(opt.get_product_id_and_good_id_by_name + f" '{product}', {good}")
# print(product_id_and_good_id_by_name.fetchval()[1])
# print(product_id_and_good_id_by_name.fetchone())


# product = 'milk'
# good = 'Capucino'
# opt = Options()
# cnc = get_connection()
# cursor = cnc.cursor()
# product_id_and_good_id = cursor.execute(opt.get_product_id_and_good_id_by_name + f" {product}, {good}")
# k = [i for i in product_id_and_good_id]
# q = k[0]
# print(q[0])




#CREATE AND GET ORDER
order = Order_repository()
order.create_order('Chel_2', 9, 'Capucino', 1)

res_o = order.get_all_orders()

for i in res_o:
    print(i)






# good_name = 'Capucino'
# opt = Options()
# cnc = get_connection()
# cursor = cnc.cursor()
# products_id_and_amount = cursor.execute(opt.get_products_amount_and_id_by_order_id + f" 8")
# for i in products_id_and_amount.fetchall():
#     print(i.product_id, i.product_amount)
#     cursor.execute(opt.update_product_amount + f" {i.product_id}, -{i.product_amount}")
#     cnc.commit()
# cnc.commit()
# good_id = cursor.execute(opt.get_good_id_by_name + f" {good_name}")
# print(good_id.fetchval())





