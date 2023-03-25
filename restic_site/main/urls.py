from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cart', views.cart),
    path('catalog', views.catalog),
    path('about', views.about),
]
