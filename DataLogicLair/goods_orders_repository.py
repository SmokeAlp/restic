
# def make_good_order(self, goods_orders):
#     try:
#         cnc = get_connection()
#         cursor = cnc.cursor()
#         query = self.__options.make_goods_orders + f" {goods_orders.order_id}, {goods_orders.good.id}, {goods_orders.good_amount} "
#         cursor.execute(query)
#         cnc.commit()
#         cnc.close()
#         print('make_goods_orders completed successfully')
#     except:
#         print('make_good_order_error')

