from django.contrib import admin
from django.urls import path,include
from .views import addproduct,cartlist

urlpatterns = [
	path('add/<int:productid>/',addproduct,name='add_product'),
	path('cart/',cartlist,name='cartlist'),
]