from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    amount = models.IntegerField(null=False)
    cost_per_amount = models.IntegerField(null=False)
    unit_of_measurement = models.CharField(max_length=12, null=False)
    def __str__(self):
        return self.name


class GoodModel(models.Model):
    name = models.CharField(max_length=50, null=False)
    amount = models.IntegerField(null=False)
    cost = models.IntegerField(null=False)
