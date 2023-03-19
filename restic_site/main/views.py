from django.shortcuts import render
from DataLogicLair.orders_repository import *
from DataLogicLair.goods_repository import *


def index(request):
    return render(request, 'main/index.html')


def cart(request):
    db_orders = Order_repository()
    db_goods = Goods_repository()
    data = {
        'orders_list': db_orders.get_all_orders(),
        'goods_list': db_goods.get_all_goods(),
    }
    return render(request, 'main/cart.html', data)
