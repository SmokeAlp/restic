from pyodbc import Error

from DataLogicLair.Models.good_input_model import get_needed_products_amount_and_id_for_good_by_good_id
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options


class Goods_repository:
    def __init__(self):
        self.__options = Options()

    def create_good(self, good):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = cursor.execute(self.__options.get_all_products_id).fetchall()
            all_pr_id = list(map(lambda x: x[0], query))
            if (good.name == '') or (good.cost < 0) or (good.products == {}):
                print('неправильно переданы данные для create_good')
                return
            gds_names = list(map(lambda x: x[1], self.get_all_goods()))
            if good.name in gds_names:
                gd_id = cursor.execute(self.__options.get_good_id_by_name + f" '{good.name}'")
                print(f'нельзя с одинаковым именем: {good} совпадает с id:{gd_id})')
                return
            query = self.__options.create_good + f" '{good.name}', {good.cost}"
            for i, b in good.products.items():
                if (type(i) is not int) or (type(b) is not int):
                    print(f'неправильно переданы данные о продуктах: {i, b}')
                    return
                elif i not in all_pr_id or b > 10 ** 3:
                    print(f'передан несуществующий продукт или слишком большое его кол-во: {i},{b}')
                    return
            cursor.execute(query)
            cnc.commit()
            cursor.execute(self.__options.get_good_id_by_name + f' {good.name}')
            good_id = cursor.fetchval()
            for i, amnt in good.products.items():
                cursor.execute(
                    self.__options.create_goods_products + f" @product_id={i},@good_id={good_id}, @product_amount={amnt}")
                cnc.commit()
            cnc.close()
            print('good have been added successfully')
        except Error as err:
            print(f'create_good_error: {err}')

    def get_all_goods_catalog(self, goods_in_cart):
        cnc = get_connection()
        cursor = cnc.cursor()
        cursor.execute(self.__options.get_all_goods)
        goods = cursor.fetchall()
        if len(goods_in_cart) > 0:
            needProducts = {}
            for good in goods_in_cart:
                for product in self.get_needed_products_amount_and_id_for_good_by_good_id(good[0].id):
                    if product.id not in needProducts.keys():
                        needProducts[product.id] = product.product_amount * good[1]
                    else:
                        needProducts[product.id] += product.product_amount * good[1]
            goodsR = []
            for good in goods:
                ok = True
                # print(good, good.id)
                # print(get_needed_products_amount_and_id_for_good_by_good_id(good.id))
                for product in get_needed_products_amount_and_id_for_good_by_good_id(good.id):
                    # print(product.id)
                    # print(get_needed_products_amount_and_id_for_good_by_good_id(8))
                    # print(product.amount, product.product_amount)
                    # print(needProducts.get(product.id), ' bebebebe')
                    if needProducts.get(product.id) == None:
                        ok = ok and product.product_amount <= product.amount
                    else:
                        ok = ok and product.product_amount + needProducts[product.id] <= product.amount
                goodsR.append([good, ok])
        else:
            goodsR = []
            for good in goods:
                ok = True
                for product in get_needed_products_amount_and_id_for_good_by_good_id(good.id):
                    ok = ok and product.product_amount <= product.amount
                goodsR.append([good, ok])
        return goodsR

    def check_add_good_in_cart_button(self, good, goods_in_cart, good_amount):
        # все данные получаются из cart_add
        cnc = get_connection()
        cursor = cnc.cursor()
        # получаю нужные продукты для товара
        cursor.execute(self.__options.get_needed_products_amount_and_id_for_good_by_good_id + f" {good.id}")
        dta = cursor.fetchall()
        # формирую словарь {id нужного продукта: его нужное кол-во }
        need_products = dict(zip([id[0] for id in dta], [nd_amnt[1]*good_amount for nd_amnt in dta]))
        print(need_products)
        # прибавляю все продукты из корзины
        for good in goods_in_cart:
            for i in self.get_needed_products_amount_and_id_for_good_by_good_id(good[0].id):
                if i.id in need_products.keys():
                    need_products[i.id] += i.product_amount * good[1]
        for product in need_products.items():
            cursor.execute(self.__options.get_product_amount_by_id + f" {product[0]}")
            product_amount_in_stock = cursor.fetchval()
            print(need_products, product_amount_in_stock)
            if product[1] > product_amount_in_stock:
                return False
        return True

    def check_cart_confirm(self, goods_in_cart):
        cnc = get_connection()
        cursor = cnc.cursor()
        need_products = {}
        for good in goods_in_cart:
            for i in self.get_needed_products_amount_and_id_for_good_by_good_id(good['good'].id):
                if i.id in need_products.keys():
                    need_products[i.id] += i.product_amount * good['amount']
                else:
                    need_products[i.id] = i.product_amount * good['amount']
        for product in need_products.items():
            cursor.execute(self.__options.get_product_amount_by_id + f" {product[0]}")
            product_amount_in_stock = cursor.fetchval()
            print(need_products, product_amount_in_stock)
            if product[1] > product_amount_in_stock:
                return False
        return True

    def get_needed_products_amount_and_id_for_good_by_good_id(self, good_id):
        cnc = get_connection()
        cursor = cnc.cursor()
        cursor.execute(
            self.__options.get_needed_products_amount_and_id_for_good_by_good_id + f" {good_id}")
        return cursor.fetchall()

    def get_all_goods(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        cursor.execute(self.__options.get_all_goods)
        goods = cursor.fetchall()
        return goods
