from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.bootstrap import InlineRadios

class RegistrationForm(UserCreationForm):
	GROUP_CHOICES= (
		("Customer","Customer"),
		("Seller","Seller")
		)
	# address= forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':3}),label="Delivery Address")
	user_type = forms.ChoiceField(required=True,widget=forms.RadioSelect,choices= GROUP_CHOICES,label="Sign Up As")
	first_name = forms.CharField(required=True,max_length=20)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ['first_name','last_name','username','password1','password2','user_type','email']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout = Layout(
				Row(
					Column('first_name',css_class='form-group col-md-6 mb-0'),
					Column('last_name',css_class='form-group col-md-6 mb-0'),
					),
				Row(
					Column('username',css_class='form-group col-md-6 mb-0'),
					Column('email',css_class='form-group col-md-6 mb-0'),
					),
				Row(
					Column('password1', css_class='form-group col-md-6 mb-0'),
					Column('password2', css_class='form-group col-md-6 mb-0')
					),
				Row(
					Column(InlineRadios('user_type'),css_class='form-group col-md-6 mb-0 container')
					),
				Submit('submit', 'Sign Up')
			)

