from pyodbc import Error

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

    def get_all_goods(self):
        cnc = get_connection()
        cursor = cnc.cursor()
        query = self.__options.get_all_goods
        cursor.execute(query)
        return cursor.fetchall()
