import datetime
from django.core.exceptions import ValidationError

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from django import forms

from .models import ProductModel
from DataLogicLair.products_repository import *




class CartAddGoodForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'amount', 'cost_per_amount', 'unit_of_measurement']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'имя продукта'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control input-lg', 'placeholder': 'кол-во продукта'}),
            'cost_per_amount': forms.NumberInput(
                attrs={'class': 'form-control input-lg', 'placeholder': 'цена за единицу продукта'}),
            'unit_of_measurement': forms.TextInput(
                attrs={'class': 'form-control input-lg', 'placeholder': 'единица измерения продукта'})
        }

    def clean_name(self):
        data = self.cleaned_data['name']
        beb = None
        try:
            beb = int(data)
            beb = True
        except:
            beb = False
        if beb:
            raise ValidationError('имя не число')
        return data

    def clean_unit_of_measurement(self):
        data = self.cleaned_data['unit_of_measurement']
        beb = None
        try:
            beb = int(data)
            beb = True
        except:
            beb = False
        if beb:
            raise ValidationError('единиц измерения не число')
        return data


class EditProductForm(forms.Form):
    name = forms.CharField()
    amount = forms.IntegerField()
    cost_per_amount = forms.IntegerField()
    choices = set([(i.unit_of_measurement, i.unit_of_measurement) for i in Product_repository().get_all_products()])
    unit_of_measurement = forms.ChoiceField(choices=choices)


products = Product_repository()
l = []
for i in products.get_all_products():
    l.append((i.id, i.name))


class TestForm(forms.Form):
    ChoiceField = forms.ChoiceField(choices=l, error_messages={'required': 'обязательное полу'},
                                    widget=forms.RadioSelect)
    MultipleChoiceField1 = forms.MultipleChoiceField(choices=l, error_messages={'required': 'обязательное полу'})
    BooleanField = forms.BooleanField(required=True)
    DateField = forms.DateField(required=False, input_formats=[datetime.datetime],
                                error_messages={'invalid': 'errorororo'})
    DateTimeField = forms.DateTimeField()
    JSONField = forms.JSONField()
    NumberInput = forms.NumberInput()
    SelectMultiple = forms.SelectMultiple()
    MultipleChoiceField2 = forms.MultipleChoiceField(choices=[('bebe', 'bebe'), ('bebe2', 'bebe2')])
    NullBooleanField = forms.NullBooleanField(
        widget=forms.RadioSelect(choices=[(None, 'None'), (True, 'Yes'), (False, 'No')]))
    RegexField = forms.RegexField(empty_value='bbe', regex='1')  # hz che eto
    TypedMultipleChoiceField = forms.TypedMultipleChoiceField(coerce=int, choices=l)
    ComboField = forms.ComboField(fields=[forms.IntegerField()], widget=forms.SelectMultiple(choices=l))
