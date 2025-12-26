from django.db import models

# Create your models here.
class Book(models.Model):
	title=models.CharField(max_length=100,blank=True)
	author=models.CharField(max_length=100,blank=True)
	isbn=models.CharField(max_length=100,blank=True)
	publisher=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.title
	
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fname+" "+self.lname