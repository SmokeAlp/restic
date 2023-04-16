from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    re_path('detail', views.cart_detail, name='cart_detail'),
    re_path('add', views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<good_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
