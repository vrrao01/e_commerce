from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=25)
	slug = models.SlugField(max_length=25,unique=True,blank=False)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=40,)
	price = models.FloatField()
	image = models.ImageField()
	category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
	description = models.TextField(max_length=1000,default="",null=False)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	placed = models.BooleanField(default=False,null=False,blank=False)
	transaction_id = models.CharField(max_length=200,null=True)

	def __str__(self):
		return f"Order-{self.id}"

	@property
	def itemcount(self):
		count = OrderItem.objects.filter(order = self).count()
		return count
	

class OrderItem(models.Model):
	product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	quantity = models.IntegerField(default=0,null=True,blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.product.name}-Order-{self.order.id}"
