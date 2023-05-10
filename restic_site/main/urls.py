from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    re_path(r'^catalog/?(?P<beb>\d+)?', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('products', views.products, name='products'),
    re_path(r'^detail/?(?P<error>\d+)?', views.cart_detail, name='cart_detail'),
    path('cart_clear', views.cart_clear, name='cart_clear'),
    path('cart_confirm', views.cart_confirm, name='cart_confirm'),
    re_path(r'^add/(?P<good_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<good_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^editProduct/(?P<product_id>\d+)/$', views.edit_products, name='edit_product'),
]
