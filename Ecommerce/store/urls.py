from django.contrib import admin
from django.urls import path,include
from .views import addproduct,cartlist,updatecart,deleteorderitem

urlpatterns = [
	path('add/<int:productid>/',addproduct,name='add_product'),
	path('cart/',cartlist,name='cartlist'),
	path('update/<int:oi_id>',updatecart,name='update_cart'),
	path('delete/<int:oi_id>',deleteorderitem,name='delete_order_item'),
]