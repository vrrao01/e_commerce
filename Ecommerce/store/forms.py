from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


QUANTITY_CHOICES = [(i,str(i)) for i in range (1,11)]

class UpdateProductQuantityForm(forms.Form):
	quantity = forms.TypedChoiceField(required=False,label="Quantity",choices = QUANTITY_CHOICES,coerce = int)

	# def __init__(self,*args,**kwargs):
	# 	super().__init__(*args,**kwargs)
	# 	self.helper = FormHelper()
	# 	self.helper.form_method = "post"
	# 	self.helper.form_action = "home:homepage"
	# 	# self.helper.add_input(Submit('submit','Update'))
	# 	self.helper.layout = Layout(
	# 		Row(
	# 			Column('quantity'),
	# 			Column(Submit('submit','Update'))
	# 			),
	# 		)