from django import forms


class CreateProductForm(forms.Form):
    name = forms.CharField(max_length=107, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'имя продукта'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'кол-во продукта'}))
    cost_per_amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'цена за определенное кол-во продукта'}))
    unit_of_measurement = forms.CharField(max_length=37, widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'единица измерения для продукта'}))

class AddProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'имя продукта'}))
    amount = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control input-lg', 'placeholder': 'кол-во продукта'}))