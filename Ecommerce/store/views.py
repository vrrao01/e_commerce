from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from .models import Product,Category,Order,OrderItem
from django.contrib.auth import get_user
from django.views.decorators.http import require_POST
from .forms import UpdateProductQuantityForm

# Create your views here.
def add_to_order(cartid,productid,quantity=1):
	curCart = Order.objects.get(pk = cartid)
	curProd = Product.objects.get(pk = productid)
	if(curCart.orderitem_set.all().filter(product = curProd).exists()):
		curOrderItem = curCart.orderitem_set.all().filter(product = curProd)[0]
		curOrderItem.quantity += quantity
		curOrderItem.save()
	else:
		newOrderItem = OrderItem(product = curProd,order = curCart,quantity = quantity)
		newOrderItem.save()

#TODO: Define an add function:
	#add(cart_id,product_id)
		#if product already in cart
			#update quantity
		#else add order_item to cart
def merge_orderitem(otherCart, orderItem):
	orderProduct = orderItem.product
	if(otherCart.orderitem_set.filter(product = orderProduct).exists()):
		oldOrderItem = otherCart.orderitem_set.filter(product = orderProduct)[0]
		oldOrderItem.quantity += orderItem.quantity
		oldOrderItem.save()
		orderItem.delete()
	else:
		orderItem.order = otherCart
		orderItem.save()

def merge_orders(sessionCartid,otherCartid):
	sessionCart = Order.objects.get(pk = sessionCartid)
	otherCart = Order.objects.get(pk = otherCartid)
	sessOrderItems = sessionCart.orderitem_set.all()
	for oi in sessOrderItems:
		merge_orderitem(otherCart,oi)
	sessionCart.delete()

@require_POST
def addproduct(request,productid):
	if('cartid' in request.session):
		print("CartID = ", request.session['cartid'])
	if (request.user.is_authenticated):
		curUser = get_user(request)
		if('cartid' in request.session):
			cartid = request.session.get('cartid')
			sessionCart = Order.objects.get(pk = cartid)
			if(Order.objects.filter(placed = False,customer = curUser).exists()):
				storedCart = Order.objects.all().filter(placed = False)[0]
				if(storedCart.id == sessionCart.id):
					add_to_order(cartid,productid,1)
				else:
					merge_orders(cartid,storedCart.id)
					request.session['cartid'] = storedCart.id
			else:
				sessionCart.customer = curUser
				sessionCart.save()
				add_to_order(cartid, productid,1)
		else:
			if(Order.objects.filter(placed = False, customer=curUser).exists()):
				storedOrder = Order.objects.filter(placed = False,customer = curUser)[0]
				request.session['cartid'] = storedOrder.id
				add_to_order(storedOrder.id,productid,1)
			else:
				newCart = Order.objects.create(customer = curUser, placed = False)
				add_to_order(newCart.id, productid,1)
				request.session['cartid'] = newCart.id 

			#if order exists in db
			#store in session 
			#add product
	else:
		if('cartid' in request.session):
			cartid = request.session.get('cartid')
			sessionCart = Order.objects.get(pk = cartid)
			add_to_order(cartid,productid,1)
		else:
			newCart = Order.objects.create(placed = False)
			add_to_order(newCart.id,productid,1)
			request.session['cartid'] = newCart.id
	return redirect(request.META.get('HTTP_REFERER')
)
		
#if request.user.is_authenticated():
	#if cart_id in session
		#prev = user.order
		#if(prev == order)
			#add product to cart_id
		#else
			#combine prev into cart_id
			#delete cart id
			#add product to cart_id
	#else
		#prev = user.order
		#if(prev exists)
			#cart_id = prev in session
		#else
			#cart_id = new user.order

		#add product to cart_id
#else
	#if cart_id in session
		#add product to cart_id
	#else 
		#create new cart
		#add product to cart
		#store cart_id in session

#TODO: Make sure the cart view has merge order function called

def cartlist(request):
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
	context = {}
	cartID = None
	if('cartid' in request.session):
		cartID = request.session.get('cartid')
	context['cart'] = OrderItem.objects.filter(order_id = cartID)
	if(context['cart'].exists()):
		context['empty'] = False
	else:
		context['empty'] = True

	context['form'] = []
	for x in context['cart']:
		form = UpdateProductQuantityForm(initial={'quantity':str(x.quantity)})
		context['form'].append(form)
	context['cart'] = zip(context['cart'],context['form'])
	cartcount = 0
	if('cartid' in request.session):
		cartcount = Order.objects.get(id = request.session.get('cartid')).itemcount
		context['ordertotal'] = Order.objects.get(id=request.session.get('cartid')).grandtotal
	context['cartcount'] = cartcount
	return render(request,'cart.html',context)




@require_POST
def updatecart(request,oi_id):
	form = UpdateProductQuantityForm(request.POST)
	oi = OrderItem.objects.get(id = oi_id)
	if(form.is_valid()):
		oi.quantity = form.cleaned_data['quantity']
		oi.save()
	return redirect('cartlist')


@require_POST
def deleteorderitem(request,oi_id):
	oi = OrderItem.objects.get(id = oi_id)
	oi.delete()
	return redirect('cartlist')