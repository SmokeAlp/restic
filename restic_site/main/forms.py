from django import forms
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLair.Models.good_model_for_order import *


class CreateProductForm(forms.Form):
    name = forms.CharField(max_length=107, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'имя продукта'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'кол-во продукта'}))
    cost_per_amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'цена за определенное кол-во продукта'}))
    unit_of_measurement = forms.CharField(max_length=37, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'единица измерения для продукта'}))

class AddProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'имя продукта'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'кол-во продукта'}))


class AddGoodInToCartForm(forms.Form):
    # def max_value_good_amount(good_id):
    #     l = list(map(lambda x: x[2] // x[1], get_needed_products_amount_and_id_for_good_by_good_id(good_id)))
    #     return min(l)

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'value':'bebe'}))
    good_amount = forms.IntegerField(min_value=1, max_value=12)