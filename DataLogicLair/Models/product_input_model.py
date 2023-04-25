class Product:
    def __init__(self, name=str, amount=int, cost_per_amount=int, unit_of_measurement=str):
        self.name = name
        self.amount = amount
        self.cost_per_amount = cost_per_amount
        self.unit_of_measurement = unit_of_measurement

    def __str__(self):
        return self.name


