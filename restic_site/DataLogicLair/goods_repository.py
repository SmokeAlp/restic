
from pyodbc import Error

from restic_site.DataLogicLair.get_conection import get_connection
from restic_site.DataLogicLair.options import Options


class Goods_repository:
    def __init__(self):
        self.__options = Options()

    def create_good(self, good):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_good + f" '{good.name}', {good.cost}"
            cursor.execute(query)
            cursor.execute(self.__options.create_goods_products + f" ")
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
