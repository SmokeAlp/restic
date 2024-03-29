class Options:
    def __init__(self):
        self.connection_string = 'DRIVER={SQL Server};SERVER=5.19.233.233\MSSQLSERVER,49172;DATABASE=restic;UID=deadinside228pro;PWD=228'
        #PRODUCTS
        self.create_product = 'exec createProducts'
        self.update_product_amount = 'exec updateProductAmount'
        self.update_product = 'exec updateProduct'
        self.delete_product = 'exec deleteProduct'
        self.get_all_products = 'exec getAllProducts'
        self.get_all_products_id = 'exec getAllProductsId'
        self.get_product_id_by_name = 'exec getProductIdByName'
        self.get_product_by_id = 'exec getProductById'
        self.check_summ_of_money_for_product_amount = 'exec checkSummOfMoneyForProductAmount'
        self.get_product_amount_by_id = 'exec getProductAmountById'
        self.get_product_name_by_id = 'exec getProductNameById'
        self.get_products_amount_and_id_by_order_id = 'exec getProductsAmountAndIdByOrderId'
        self.get_needed_products_amount_and_id_for_good_by_good_id = "exec getNeededProductsAmountAndIdForGoodByGoodId"
        self.get_goods_from_carts_by_product_id = f"exec getGoodsFromCartsByProductId"
        #GOODS
        self.get_all_goods = 'exec getAllGoods'
        self.create_good = 'exec createGoods'
        self.get_good_id_by_name = 'exec getGoodIdByName'
        #ORDERS
        self.get_all_orders = 'exec getAllOrders'
        self.get_last_order_id = 'exec getLastOrderId'
        self.create_order = 'exec createOrders'
        self.check_availability_of_customer = 'exec checkAvailabilityOfCustomer'
        #CUSTOMERS
        self.create_customer = 'exec createCustomers'
        self.get_all_customer = 'exec getAllCustomers'
        self.get_all_customers_name = 'exec getAllCustomersName'
        self.update_customer_summ_money = 'exec updateCustomerSummMoney'
        #CUSTOMERS_ORDERS
        self.create_customers_orders = 'exec createCustomersOrders'
        #GOODS_PRODUCTS
        self.create_goods_products = 'exec createGoodsProducts'
        self.get_all_goods_products = 'exec getAllGoodsProducts'
        self.get_product_id_and_good_id_by_name = 'exec getProductIdAndGoodIdByName'
        #GOODS_ORDERS
        self.create_goods_orders = 'exec createGoodsOrder'
