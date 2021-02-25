from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User,Group
from .decorators import not_logged_in
from django.views.generic import UpdateView, DetailView
from django.shortcuts import reverse

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
			# deliveryaddress = form.cleaned_data['address']
			# user.userprofile.address = deliveryaddress
			user.userprofile.save()
			return redirect('login')
	context ={'form':form,}
	return render(request,template_name,context)

class UpdateProfileView(UpdateView):
	model = User
	fields = ['username','first_name','last_name']
	template_name = 'accounts/editprofile.html'
	context_object_name = 'userprofile'

	def get_success_url(self):
		return reverse('profile')

	def get_object(self):
		return get_object_or_404(User,username=self.request.user.username)


class UserProfileView(DetailView):
	model = User
	context_object_name = 'userprofile'
	template_name = 'accounts/profile.html'

	def get_object(self):
		return get_object_or_404(User,username= self.request.user.username)