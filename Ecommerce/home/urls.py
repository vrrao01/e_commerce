"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.http import require_GET
from .views import Homepage,ProductDetail,CategoryList,SearchList
app_name = "home"
urlpatterns = [
    path('', Homepage.as_view(),name="homepage"),
    path('product/<int:pk>/',ProductDetail.as_view(),name="product_detail"),
    path('category/<str:slug>/',CategoryList.as_view(),name="category_list"),
    path('search/',require_GET(SearchList.as_view()),name="search_products")
]
