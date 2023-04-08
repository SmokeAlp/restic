import datetime


from django import forms
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from DataLogicLair.products_repository import *
from DataLogicLair.goods_repository import *

products = Product_repository()
l = []
for i in products.get_all_products():
    l.append((i.id, i.name))

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



class TestForm(forms.Form):
    ChoiceField = forms.ChoiceField(choices=l, error_messages={'required': 'обязательное полу'}, widget=forms.RadioSelect)
    MultipleChoiceField1 = forms.MultipleChoiceField(choices=l, error_messages={'required': 'обязательное полу'})
    BooleanField = forms.BooleanField(required=True)
    DateField = forms.DateField(required=False, input_formats=[datetime.datetime], error_messages={'invalid': 'errorororo'})
    DateTimeField = forms.DateTimeField()
    JSONField = forms.JSONField()
    NumberInput = forms.NumberInput()
    SelectMultiple = forms.SelectMultiple()
    MultipleChoiceField2 = forms.MultipleChoiceField(choices=[('bebe','bebe'),('bebe2','bebe2')])
    NullBooleanField = forms.NullBooleanField(widget=forms.RadioSelect(choices=[(None, 'None'), (True, 'Yes'), (False,'No')]))
    RegexField = forms.RegexField(empty_value='bbe', regex='1') #hz che eto
    TypedMultipleChoiceField = forms.TypedMultipleChoiceField(coerce=int, choices=l)
    ComboField = forms.ComboField(fields=[forms.IntegerField()], widget=forms.SelectMultiple(choices=l))