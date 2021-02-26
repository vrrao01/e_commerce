from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from store.models import Product,Category
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

