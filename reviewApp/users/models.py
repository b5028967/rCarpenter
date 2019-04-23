from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	first_name = models.CharField(default = '', max_length = 30)
	last_name = models.CharField(default = '', max_length = 30)
	date_of_birth = models.DateField(default = timezone.now)
	address = models.CharField(default = '', max_length = 225)
	city = models.CharField(default = '', max_length = 100)
	country = models.CharField(default = '', max_length = 100)

	def __str__(self):
		return f'Profile for {self.user.username}'
