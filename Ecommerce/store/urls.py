from django.contrib import admin
from django.urls import path,include
from .views import addproduct

urlpatterns = [
	path('add/<int:productid>/',addproduct,name='add_product')
]