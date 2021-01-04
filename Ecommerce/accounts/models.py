from django.db import models
from django.contrib.auth.models import User,Group
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	address = models.CharField(blank=True,max_length =300,default="")

	def __str__(self):
		return f"{self.user.first_name}"