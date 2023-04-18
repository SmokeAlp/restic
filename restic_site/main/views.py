from django.shortcuts import render, redirect, get_object_or_404
import os
import sys

from .forms import *

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from DataLogicLair.orders_repository import *
from DataLogicLair.goods_repository import *
from DataLogicLair.products_repository import *
from DataLogicLair.Models.product_input_model import *

from django.views.decorators.http import require_POST
from .models import GoodModel

from .cart import Cart
from .forms import CartAddGoodForm

product_repo = Product_repository()


def index(request):
    return render(request, 'main/index.html')


# def cart(request):
#     data = {
#         'orders_list': ordersInCart,
#         'goods_list': "bbebebebe",
#     }
#     return render(request, 'main/cart.html', data)


def catalog(request):
    db_goods = Goods_repository()
    if request.POST:
        form = CartAddGoodForm(request.POST)
        if form.is_valid():
            values = {
                'name': form.cleaned_data.get('name'),
                'amount': form.cleaned_data.get('amount')
            }
            print(values.get('name'), values.get('amount'))
    else:
        form = CartAddGoodForm()
    data = {
        # проверка
        'goods_list': db_goods.get_all_goods_cart(),
        'form': form,
    }
    return render(request, 'cart/catalog.html', data)


def about(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.data
            print(data)
        else:
            print(form.errors)
    else:
        form = ProductForm()
    return render(request, 'main/about.html', {'form': form})


def admin_panel(request):
    errors = {}
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            values = {
                'name': form.cleaned_data.get('name'),
                'amount': form.cleaned_data.get('amount'),
                'cost_per_amount': form.cleaned_data.get('cost_per_amount'),
                'unit_of_measurement': form.cleaned_data.get('unit_of_measurement')
            }
            for i in values.values():
                try:
                    beb = int(i)
                except:
                    errors[i] = 'Error'
                print(i, type(i))
            print(errors)
            pr = Product(values.get('name'), values.get('amount'), values.get('cost_per_amount'),
                         values.get('unit_of_measurement'))
            print(pr)
            # product_repo.create_product(pr)
            # print(type(pr_rep.create_product(pr)[0]))
    else:
        form = CreateProductForm()
    return render(request, 'main/admin_panel.html', {"form": form})


@require_POST
def cart_add(request, good_id):
    goods_rep = Goods_repository()
    goods = goods_rep.get_all_goods()
    cart = Cart(request)
    good = None
    for item in goods:
        if item.id == int(good_id):
            good = item
    form = CartAddGoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(good=good,
                 amount=cd['amount'],
                 update_amount=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, good_id):
    goods_rep = Goods_repository()
    goods = goods_rep.get_all_goods()
    cart = Cart(request)
    good = None
    for item in goods:
        if item.id == int(good_id):
            good = item
    cart.remove(good)
    return redirect('cart_detail')


def products(request):
    return render(request, 'main/products.html', {'products': Product_repository().get_all_products()})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
