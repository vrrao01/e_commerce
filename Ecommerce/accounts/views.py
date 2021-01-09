from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User,Group
from .decorators import not_logged_in
# Create your views here.
@not_logged_in
def registration(request):
	template_name= "registration/signup.html"
	form = RegistrationForm()
	if request.method=="POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name=form.cleaned_data['user_type'])
			user.groups.add(group)
			deliveryaddress = form.cleaned_data['address']
			user.userprofile.address = deliveryaddress
			user.userprofile.save()
			return redirect('login')
	context ={'form':form,}
	return render(request,template_name,context)

