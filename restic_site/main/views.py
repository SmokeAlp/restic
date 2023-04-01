from django.shortcuts import render, redirect
import os
import sys

from django.views.generic import ListView

from .forms import *
from .utils import check_products_for_goods

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DataLogicLair.orders_repository import *
from DataLogicLair.goods_repository import *
from DataLogicLair.products_repository import *
from DataLogicLair.Models.product_input_model import *


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


def catalog(request):
    db_goods = Goods_repository()
    g = check_products_for_goods()
    data = {
        'goods_list': db_goods.get_all_goods(),
    }
    return render(request, 'main/catalog.html', data)


def about(request):
    return render(request, 'main/about.html')


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
            print(pr)
            pr_rep = Product_repository()
            pr_rep.create_product(pr)
            if not pr_rep.create_product(pr):
                form['error'] = pr_rep.create_product(pr)
    else:
        form = CreateProductForm()
    return render(request, 'main/admin_panel.html', {"cr_pr_form": form})
