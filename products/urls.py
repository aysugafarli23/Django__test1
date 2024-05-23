from django.urls import path
from  . import views

#products
#products/1/detail
#producst/new
urlpatterns = [
    path('', views.index),
    path('news', views.products_news),
    path('1',views.product1),
    path('2', views.product2),
    path('3',views.product3)
]
