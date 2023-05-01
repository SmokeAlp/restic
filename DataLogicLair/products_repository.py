from pyodbc import Error
from DataLogicLair.get_conection import get_connection
from DataLogicLair.options import Options


class Product_repository:
    def __init__(self):
        self.__options = Options()

    def create_product(self, product):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            prs_names = list(map(lambda x: x[1], self.get_all_products()))
            if product.name in prs_names:
                pr_id = cursor.execute(self.__options.get_product_id_by_name + f" '{product.name}'").fetchval()
                # print(f'нельзя с одинаковым именем: {product} совпадает с id:{pr_id}')
                return f'нельзя с одинаковым именем: {product} совпадает с id:{pr_id}', False
            if product.amount < 0:
                # print(f'отрицательное значение количества продукта:{product.amount}')
                return f'отрицательное значение количества продукта:{product.amount}'
            query = self.__options.create_product + f" '{product.name}'," \
                                                    f" {product.amount}," \
                                                    f" {product.cost_per_amount}," \
                                                    f" {product.unit_of_measurement}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('product have been created successfully')
            return True
        except Error as err:
            print(f'create_products_error: {err}')

    def add_product(self, product_name=str, amount=int):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            product_id = cursor.execute(self.__options.get_product_id_by_name + f" {product_name}")
            query = self.__options.update_product_amount + f" {product_id.fetchval()}, {amount}"
            cursor.execute(query)
            cnc.commit()
            cnc.close()
            print('product have been added successfully')
            return True
        except Error as err:
            print(f'create_products_error: {err}')

    def delete_product(self, product_id=int):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            cursor.execute(self.__options.get_goods_from_carts_by_product_id + f" {product_id}")
            if len(cursor.fetchall()) != 0:
                print('у кого-то в корзине есть товар с таким продуктом')
                return
            else:
                cursor.execute(self.__options.delete_product + f" {product_id}")
                cursor.commit()
                cursor.close()
                print('product have been deleted successfully')
                return True
        except Error as err:
            print(f'delete product error: {err}')

    def edit_product(self, product_id, product):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            if product.amount < 0 or product.cost_per_amount < 0:
                return False
            cursor.execute(self.__options.update_product + f" {product_id},"
                                                           f"'{product.name}',"
                                                           f"{product.amount},"
                                                           f"{product.cost_per_amount},"
                                                           f"'{product.unit_of_measurement}'")
            cursor.commit()
            cursor.close()
            return True
        except Error as err:
            print(f'edit product error: {err}')

    def get_all_products(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_products
        cursor.execute(query)
        return cursor.fetchall()

    def check_summ_of_money_for_product_amount(self, product_name=str, amount=int):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.get_product_id_by_name + f" {product_name}"
            product_id = cursor.execute(query)
            cursor.execute(
                self.__options.check_summ_of_money_for_product_amount + f" {product_id.fetchval()}, {amount}")
            return str(cursor.fetchval()) + ' рублей'
        except Error as err:
            print(f'create_products_error: {err}')
