from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('products', views.products, name='products'),
    path('cart_confirm', views.cart_clear, name='cart_clear'),
    re_path('detail', views.cart_detail, name='cart_detail'),
    re_path(r'^add/(?P<good_id>\d+)/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<good_id>\d+)/$', views.cart_remove, name='cart_remove'),
    re_path(r'^editProduct/(?P<product_id>\d+)/$', views.editProducts, name='edit_product'),
]
