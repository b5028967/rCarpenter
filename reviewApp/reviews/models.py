from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	name = models.CharField(default = '', max_length = 225)
	brand = models.CharField(default = '', max_length = 225)
	avg_cost = models.DecimalField(default = 000.00, max_digits = 5, decimal_places = 2)
	category = models.CharField(default = '', max_length = 225)
	date_released = models.DateField(default = timezone.now)
	description = models.TextField()
	photo = models.ImageField(default = 'default.jpg', upload_to = 'product_pics')

	def __str__(self):
		return self.name

class Review(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	rating = models.IntegerField(default = 0, max_length = 5)
	review_text = models.TextField()
	date = models.DateField(default = timezone.now)

	def __str__(self):
		return f'The review of {self.product.name}'


