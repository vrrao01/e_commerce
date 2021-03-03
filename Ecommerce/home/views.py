from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from store.models import Product,Category,Order
from django.views.generic.detail import DetailView

# Create your views here.

# def home(request):
# 	return render(request,"home/homepage.html")
# 	

class Homepage(ListView):
	model = Product
	template_name = 'home/homepage.html'
	context_object_name = 'products'


	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		return context

class ProductDetail(DetailView):
	template_name = 'home/product.html'
	model = Product
	context_object_name = 'product'


	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		return context

class CategoryList(DetailView):

	context_object_name = "given_cat"
	model = Category
	template_name = 'home/category.html'

	def get_queryset(self,**kwargs):
		print("given slug",self.kwargs['slug'])
		return Category.objects.all().filter(slug = self.kwargs['slug'])


	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		return context