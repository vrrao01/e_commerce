from django.shortcuts import render,redirect

def not_logged_in(view_function):
	def wrapper(request,*args,**kwargs):
		if request.user.is_authenticated:
			return redirect('home:homepage')
		else:
			return view_function(request,*args,**kwargs)

	return wrapper