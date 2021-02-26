from django.db import models

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


	def __str__(self):
		return self.name

