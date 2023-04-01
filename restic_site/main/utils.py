
from DataLogicLair.Models.good_model_for_order import Good_for_order


def check_products_for_goods(goods):
    needProducts = {}
    for i in goods:
        for product in i.get_needed_products_amount_and_id_for_good_by_good_id():
            print(product)
            if product.id not in needProducts.keys():
                needProducts[product.id] = [product.product_amount * i.amount, product.amount, i.get_good_id_by_name()]
            else:
                needProducts[product.id][0] += product.product_amount * i.amount
    print(needProducts)
    haventGoodds = []
    problems_goods = {}
    for k, v in needProducts.items():
        if v[0] > v[1]:
            if v[2] not in haventGoodds:
                haventGoodds.append(v[2])
                problems_goods[k] = [v[1]]
    print(haventGoodds, 'bebe')
    return haventGoodds

good_for_order_1 = Good_for_order('Capucino', 500000000)
good_for_order_2 = Good_for_order("Salad", 1000000)
good_for_order_3 = Good_for_order("Salad_2", 1000000000)
good_for_order_4 = Good_for_order("fried potato", 1000000000)
good_for_order_5 = Good_for_order("Pork Steak", 1000000000)
good_for_order_6 = Good_for_order("Donut", 1000000000)
goods = [good_for_order_1, good_for_order_2,good_for_order_3,good_for_order_4, good_for_order_5,good_for_order_6]


g = check_products_for_goods(goods)
print(g)