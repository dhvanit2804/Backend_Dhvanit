from rest_framework import serializers
from .models import Book,User


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model=Book
		fields=('id','title','author','isbn','publisher')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id','fname','lname','email','password')