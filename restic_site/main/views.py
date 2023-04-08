from django.shortcuts import render, redirect
import os
import sys


from .forms import *


sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DataLogicLair.orders_repository import *
from DataLogicLair.goods_repository import *
from DataLogicLair.products_repository import *
from DataLogicLair.Models.product_input_model import *


product_repo = Product_repository()

def index(request):
    return render(request, 'main/index.html')


def cart(request):
    data = {
        'orders_list': ordersInCart,
        'goods_list': "bbebebebe",
    }
    return render(request, 'main/cart.html', data)


def catalog(request):
    db_goods = Goods_repository()
    if request.POST:
        form = AddGoodInToCartForm(request.POST)
        if form.is_valid():
            values = {
                'name': form.cleaned_data.get('name'),
                'amount': form.cleaned_data.get('amount')
            }
            print(values.get('name'), values.get('amount'))
    else:
        form = AddGoodInToCartForm()
    data = {
        # проверка
        'goods_list': db_goods.get_all_goods(),
        'form': form
    }
    return render(request, 'main/catalog.html', data)


def about(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.items()
            for i in data:
                print(i[1], type(i[1]))
            print(type(data), data)
        else:
            print(form.errors)
    else:
        form = TestForm()
    return render(request, 'main/about.html', {'form': form})


def admin_panel(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            values = {
                'name': form.cleaned_data.get('name'),
                'amount': form.cleaned_data.get('amount'),
                'cost_per_amount': form.cleaned_data.get('cost_per_amount'),
                'unit_of_measurement': form.cleaned_data.get('unit_of_measurement')
            }
            pr = Product(values.get('name'), values.get('amount'), values.get('cost_per_amount'), values.get('unit_of_measurement'))
            # product_repo.create_product(pr)
            # print(type(pr_rep.create_product(pr)[0]))
        else:
            ...
    else:
        form = CreateProductForm()
    return render(request, 'main/admin_panel.html', {"form": form})


