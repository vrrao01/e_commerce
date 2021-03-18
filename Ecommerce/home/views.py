from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from store.models import Product,Category,Order
from django.views.generic.detail import DetailView
from accounts.models import UserProfile
from django.contrib.auth.models import User
from store.views import merge_orders
from django.contrib.auth import get_user
from store.models import Order
# Create your views here.

# def home(request):
# 	return render(request,"home/homepage.html")
# 	

def fetchcart(request):
	if (request.user.is_authenticated):
		curUser = get_user(request)
		if('cartid' in request.session):
			cartid = request.session.get('cartid')
			sessionCart = Order.objects.get(pk = cartid)
			if(Order.objects.filter(placed = False,customer = curUser).exists()):
				storedCart = Order.objects.all().filter(placed = False)[0]
				if(storedCart.id != sessionCart.id):
					merge_orders(cartid,storedCart.id)
					request.session['cartid'] = storedCart.id
			else:
				sessionCart.customer = curUser
				sessionCart.save()
		else:
			if(Order.objects.filter(placed = False, customer=curUser).exists()):
				storedOrder = Order.objects.filter(placed = False,customer = curUser)[0]
				request.session['cartid'] = storedOrder.id

class Homepage(ListView):
	model = Product
	template_name = 'home/homepage.html'
	context_object_name = 'products'


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		fetchcart(self.request)
		cartcount = 0
		if('cartid' in self.request.session):
			cartcount = Order.objects.get(id = self.request.session.get('cartid')).itemcount
		context['cartcount'] = cartcount
		return context

class ProductDetail(DetailView):
	template_name = 'home/product.html'
	model = Product
	context_object_name = 'product'


	def get_context_data(self,**kwargs):

		context = super().get_context_data(**kwargs)
		context['categories'] = list(Category.objects.all())
		cartcount = 0
		if('cartid' in self.request.session):
			cartcount = Order.objects.get(id = self.request.session.get('cartid')).itemcount
		context['cartcount'] = cartcount
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
		cartcount = 0
		if('cartid' in self.request.session):
			cartcount = Order.objects.get(id = self.request.session.get('cartid')).itemcount
		context['cartcount'] = cartcount
		return context