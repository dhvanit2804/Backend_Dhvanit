from django.shortcuts import render
from rest_framework import generics
from .models import Book,User
from .seriazlizers import BookSerializer,UserSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
	queryset=Book.objects.all()
	serializer_class=BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Book
	serializer_class=BookSerializer

class UserList(generics.ListCreateAPIView):
	queryset=User.objects.all()
	serializer_class=UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=User
	serializer_class=UserSerializer