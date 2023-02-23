from DataLogicLair.get_conection import *
from mysql.connector import Error

class Goods_repository:
    def __init__(self):
        self.__options = Options()

    def create_good(self, good):
        try:
            cnc = get_connection()
            cursor = cnc.cursor()
            query = self.__options.create_good + f" '{good.name}', {good.cost}"
            cursor.execute(query)
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
