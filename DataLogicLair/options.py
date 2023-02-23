class Options:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=5.19.233.233\MSSQLSERVER,49172;DATABASE=restic;UID=deadinside228pro;PWD=228'
        #PRODUCTS
        self.create_product = 'exec createProducts'
        self.update_product_amount = 'exec updateProductAmount'
        self.get_all_products = 'exec getAllProducts'
        self.get_product_id_by_name = 'exec getProductIdByName'
        #GOODS
        self.get_all_goods = 'exec getAllGoods'
        self.create_good = 'exec createGoods'
        self.get_good_id_by_name = 'exec getGoodIdByName'
        #ORDERS
        self.get_all_orders = 'exec getAllOrders'
        self.create_order = 'exec createOrders'
        #GOODS_PRODUCTS
        self.create_goods_products = 'exec createGoodsProducts'
        self.get_all_goods_products = 'exec getAllGoodsProducts'
        self.get_product_id_and_good_id_by_name = 'exec getProductIdAndGoodIdByName'
        #GOODS_ORDERS (пока не задействуется)
        self.create_goods_orders = 'exec create_Goods_Orders'


