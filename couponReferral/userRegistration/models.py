from django.db import models

# Create your models here.

class UserRegistration(models.Model):
	"""docstring for UserREgistration"""
	username=models.CharField(max_length=30)
	password=models.CharField(max_length=30,default="")
	email=models.EmailField(max_length = 254) 
	age=models.IntegerField() 
	city=models.CharField(max_length=30)
	referral_code=models.CharField(max_length=7)


	# def __init__(self, arg):
	# 	super(UserREgistration, self).__init__()
	# 	self.arg = arg

	def __str__(self):
		return self.username
		