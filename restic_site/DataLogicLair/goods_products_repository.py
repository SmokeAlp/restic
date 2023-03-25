
from pyodbc import Error

from restic_site.DataLogicLair.get_conection import get_connection
from restic_site.DataLogicLair.options import Options


class Goods_products_repository:
    def __init__(self):
        self.__options = Options()

    def create_goods_products(self, product, good, product_amount):
        try:
            global pr_id, gd_id
            cnc = get_connection()
            cursor = cnc.cursor()
            get_product_id_and_good_id_by_name = cursor.execute(self.__options.get_product_id_and_good_id_by_name + f" '{product}', '{good}'")
            for id in get_product_id_and_good_id_by_name:
                pr_id = id[0]
                gd_id = id[1]
            query = self.__options.create_goods_products + f" {pr_id}, {gd_id}, {product_amount}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('goods_product have been done successfully')
        except Error as err:
            print(f'goods_products_error:{err}')

    # 2 METHOD
    # def create_goods_products(self, product, good, product_amount):
    #     try:
    #         print(product, good)
    #         cnc = get_connection()
    #         cursor = cnc.cursor()
    #         get_product_id_by_name = cursor.execute(self.__options.get_product_id_by_name + f" {product}")
    #         pr_id = [i.id for i in get_product_id_by_name]
    #         get_good_id_by_name = cursor.execute(self.__options.get_good_id_by_name + f" {good}")
    #         gd_id = [i.id for i in get_good_id_by_name]
    #         query = self.__options.create_goods_products + f" {pr_id}, {gd_id}, {product_amount}"
    #         cursor.execute(query)
    #         cnc.commit()
    #         cnc.close()
    #         print('goods_product have been done successfully')
    #     except Error as err:
    #         print(f'goods_products_error: {err}')

    def get_all_goods_products(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_goods_products
        cursor.execute(query)
        return cursor.fetchall()
