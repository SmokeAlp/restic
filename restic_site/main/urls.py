from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('cart', views.cart, name='cart'),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
]
