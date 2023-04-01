from DataLogicLair.Models.good_model_for_order import *
from DataLogicLair.Models.good_input_model import Good
from DataLogicLair.Models.product_input_model import *
from DataLogicLair.goods_repository import Goods_repository
from DataLogicLair.products_repository import *

# CREATE AND GET AND ADD PRODUCT
# product = Product_repository()
# product_model = Product('cake', 1200, 45, 'shtuka')
# product.create_product(product_model)
#
# product.add_product('Apple', 10)
# res = product.get_all_products()
#
# for i in res:
#     print(i)





# CREATE AND GET GOOD
# good = Goods_repository()
# pr = Product_repository()
# l = list(map(lambda x:x[1],pr.get_all_products()))
# p = 'potato'
# print(p in l)


# good_model = Good('Beef', 126, {10: 10, 4: 2})
# print(good_model)
# good.create_good(good_model)
#
# res = good.get_all_goods()
#
# for i in res:
#     print(i)

# if (good_model.name == '') or (good_model.cost < 0) or (good_model.products == {}):
#     print('неправильно переданы данные для create_good')
# for i,b in good_model.products.items():
#     if (type(i) is not int) or (type(b) is not int):
#         print(f'неправильно переданы данные о продуктах: {i,b}')
#         break
#     elif i not in all_pr_id or b>10**3:
#         print(f'передан несуществующий продукт или слишком большое его кол-во: {i},{b}')
#         break
# for i in good.get_all_goods():
#     print(i)
#     beb = True
#     if i.name == good_model.name:
#         print(f'нельзя с одинаковым именем: {good_model} совпадает с {i.name}(id:{i.id}) ')
#         beb = False
#         break
# if beb:
#     good.create_good(good_model)

# for i in good.get_all_goods():
#     print(i)








# CREATE AND GET GOODS_PRODUCTS
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


# opt = Options()











# CREATE AND GET ORDER
# order = Order_repository()
# order_model = Order(1, 'Capucino', 1)
#
# order.create_order(order_model)

# customer = Customer_repository()
# cnc = get_connection()
# cursor = cnc.cursor()
# # cursor.execute(opt.get_good_id_by_name + f" {order_model.good_name}")
# # good_id = cursor.fetchval()
# # print(good_id)
# # cursor.execute(
# #     opt.get_last_order_id
# # )
# # ord_id = cursor.fetchval()
# # print(ord_id)
# # query = opt.create_goods_orders + f" {good_id}, {ord_id}, {order_model.good_amount}"
# # cursor.execute(query)
# # cnc.commit()
# # cursor.execute(opt.get_products_amount_and_id_by_order_id + f" {ord_id}")
# # products_id_and_amount = cursor.fetchall()
# # print(products_id_and_amount)
# # for i in products_id_and_amount:
# #     print(i.product_id, i.product_amount)
# #     cursor.execute(opt.update_product_amount + f" {i.product_id}, -{i.product_amount}")
# #     cnc.commit()
# cursor.execute(opt.update_customer_summ_money + f" {order_model.customer_id}")
# cnc.commit()
# res = customer.get_all_customer()
# for i in res:
#     print(i)
# if __name__ == '__main__':
#
#     res_o = order.get_all_orders()
#
#     for i in res_o:
#         print(i)

# cust = Customer_repository()
# cust_model = Customer('QWEQWE')
#
# cust.create_customer(cust_model)
# res = cust.get_all_customer()
# for i in res:
#     print(i)


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


options = Options()
good_for_order_1 = Good_for_order('Capucino', 1)
good_for_order_2 = Good_for_order("Salad", 100)
goods = [good_for_order_1, good_for_order_2]

cnc = get_connection()
cursor = cnc.cursor()
order = {
    "cust_name": "Bebra",
    "goods": goods
}
cust_names = cursor.execute(options.get_all_customers_name).fetchall()
c_n = list(map(lambda x: x[0], cust_names))
print(c_n)
if order.get("cust_name") in c_n:
    print("Такой покупатель существует")
# else:
#     cursor.execute(options.create_customer + f" {order.get('cust_name')}")
#     cnc.commit()
#     cursor.execute(options.get_all_customer)
#     c = cursor.fetchall()
#     print(c)
#
# # print(good_for_order_1.get_good_id_by_name())
# # print(good_for_order_1.get_needed_products_amount_and_id_for_good_by_good_id())
#
#
# # glsit2 = {}
# # praalistglav = {}
# # # {name: capcino, amount: 1}
# # for i in order.get("goods"):
# #     npr = i.get_needed_products_amount_and_id_for_good_by_good_id()
# #     pramlist = []
# #     for k in npr:
# #         print(k.id, k.product_amount)
# #         cursor.execute(options.get_product_amount_by_id + f" {k.id}")
# #         spram = cursor.fetchval()
# #         print(spram)
# #         rna = k.product_amount * i.amount
# #         print(rna)
# #         if rna > spram:
# #             pramlist.clear()
# #             break
# #         pramlist.append(k.id)
# #         pramlist.append(rna)
# #     if pramlist != []:
# #         for j in pramlist:

print(good_for_order_1.get_needed_products_amount_and_id_for_good_by_good_id())
glist1 = []
needProducts = {}
productAmount = {}
for i in order.get('goods'):
    for product in i.get_needed_products_amount_and_id_for_good_by_good_id():
        print(product)
        if product.id not in needProducts.keys():
            needProducts[product.id] = [product.product_amount * i.amount, product.amount]
        else:
            needProducts[product.id][0] += product.product_amount * i.amount
print(needProducts)
haventGoodds = []
problems_goods = {}
for k,v in needProducts.items():
    if v[0] > v[1]:
        haventGoodds.append(k)
        problems_goods[k] = [v[1]]
print(haventGoodds)
if len(haventGoodds) == 0:
    print('ok')
else:
    for i in order.get('goods'):
        pr_nd_id_for_gd = list(map(lambda x: x[0], i.get_needed_products_amount_and_id_for_good_by_good_id()))
        print(pr_nd_id_for_gd)
        probl = list(set(pr_nd_id_for_gd) & set(haventGoodds))
        if len(probl) > 0:
            for k in probl:
                problems_goods[k].append(i.name)
                problems_goods[k].append(i.amount)

print(problems_goods)
for k,v in problems_goods.items():
    print(f'проблема с прод {k}({v[0]} на складе) для товаров:{v[1::3]}(нужно {v[3::3]} продуктоы для {v[2::3]} {v[1::3]}')


# for k in range(i.amount):
#     glist1.append(i.get_needed_products_amount_and_id_for_good_by_good_id())
#
#
# haventGoodds = []
# productsForOrder = {}
# for i in glist1:
#     for k in i:
#         if k.id not in productsForOrder.keys():
#             productsForOrder[k.id] = k.amount
#             print(productsForOrder)
#         if productsForOrder[k.id] > k.product_amount:
#             productsForOrder[k.id] -= k.product_amount
#         else:
#             haventGoodds.append(k.id)
#
# if len(haventGoodds) > 0:
#     print(haventGoodds)
#     print("bebebe")

# for i in order.get('goods'):
#     print(i.name, i.amount)
# if glsit2 == order.get("goods"):
#     for i in glsit2:
#         query = options.create_order
#         cursor.execute(query)
#         cnc.commit()
#         cursor.execute(options.get_last_order_id)
#         order_id = cursor.fetchval()
#         query = options.create_customers_orders + f" {order_id}, {order.customer_id}"
#         cursor.execute(query)
#         cnc.commit()
#         cursor.execute(self.__options.get_good_id_by_name + f" {order.good_name}")
#         good_id = cursor.fetchval()
#         query = self.__options.create_goods_orders + f" {good_id}, {order_id}, {order.good_amount}"
#         cursor.execute(query)
#         cnc.commit()
#         cursor.execute(self.__options.get_products_amount_and_id_by_order_id + f" {order_id}")
#         products_id_and_amount = cursor.fetchall()
#         for i in products_id_and_amount:
#             cursor.execute(self.__options.get_product_amount + f" {i.product_id}")
#             pr_am_in_stock = cursor.fetchval()
#             cursor.execute(self.__options.get_product_name_by_id + f' {i.product_id}')
#             pr_name = cursor.fetchval()
#             if pr_am_in_stock < i.product_amount:
#                 print(f'не хватает {pr_name}, нужно больше денег денег денег денег денег для {pr_name}')
#                 return False
#         for i in products_id_and_amount:
#             print(i.product_id, i.product_amount)
#             cursor.execute(self.__options.update_product_amount + f" {i.product_id}, -{i.product_amount}")
#             cnc.commit()
#         cursor.execute(self.__options.update_customer_summ_money + f" {order.customer_id}")
#         cnc.commit()
#         cnc.close()
#         print('order have been added successfully, products_amount have been update successfuly, earned money have been update successfuly')
