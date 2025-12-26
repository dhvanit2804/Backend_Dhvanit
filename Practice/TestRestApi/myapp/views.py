from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    if request.method=="POST":
        url="http://localhost:8000/api/books"
        querystring={'title':request.POST['title'],'author':request.POST['author'],'isbn':request.POST['isbn'],'publisher':request.POST['publisher']}
        response=requests.post(url,json=querystring)
        print(response)
        msg="Data Inserted Successfully"
        response=requests.get(url)
        data=response.json()
        return render(request, 'index.html',{'data':data, 'msg':msg})
    else:
        url="http://localhost:8000/api/books"
        response=requests.get(url)
        data=response.json()
        return render(request, 'index.html',{'data':data})
    
def user(request):
    if request.method=="POST":
        url="http://localhost:8000/api/user"
        querystring={'fname':request.POST['fname'],'lname':request.POST['lname'],'email':request.POST['email'],'password':request.POST['password']}
        res=requests.post(url,json=querystring)
        print(res)
        msg="User Registered Successfully"
        res=requests.get(url)
        data=res.json()
        return render(request, 'user.html', {'data':data, 'msg':msg})
    else:
        url="http://localhost:8000/api/user"
        res=requests.get(url)
        data=res.json()
        return render(request, 'user.html',{'data':data})