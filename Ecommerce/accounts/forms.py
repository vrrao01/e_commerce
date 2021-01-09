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
	address= forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':3}),label="Delivery Address")
	user_type = forms.ChoiceField(required=True,widget=forms.RadioSelect,choices= GROUP_CHOICES,label="Sign Up As")
	first_name = forms.CharField(required=True,max_length=20)
	class Meta:
		model = User
		fields = ['first_name','last_name','username','address','password1','password2','user_type']
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.layout = Layout(
				Row(
					Column('first_name',css_class='form-group col-md-6 mb-0'),
					Column('last_name',css_class='form-group col-md-6 mb-0'),
					),
				Row(
					Column('address',css_class='form-group col-md-6 mb-0'),
					Column(InlineRadios('user_type'),css_class='form-group col-md-6 mb-0')
					),
				Row(
					Column('username', css_class='form-group col-md-4 mb-0'),
					Column('password1', css_class='form-group col-md-4 mb-0'),
					Column('password2', css_class='form-group col-md-4 mb-0')
					),
				Submit('submit', 'Sign Up')
			)

