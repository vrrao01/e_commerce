from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Product,Category

# Create your views here.
class ProductDetail(DetailView):
	template_name = 'home/product.html'
	model = Product
	context_object_name = 'product'


	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		return context
