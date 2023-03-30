class Good:
    def __init__(self, name=str, cost=int, products=dict):
        self.name = name
        self.cost = cost
        self.products = products

    def __str__(self):
        return self.name
