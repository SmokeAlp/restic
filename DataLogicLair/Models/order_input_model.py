class Order:
    def __init__(self, customer_name=str, goods_list=list):
        self.order = {
            "customer_name": customer_name,
            "goods": goods_list
        }