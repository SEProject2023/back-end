from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == "POST":
        print(request.POST.get("username"))
        print(request.POST.get("password"))

        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            request.session['username'] = request.POST.get("username")
            return render(request,'welcome.html',{"username":request.POST.get("username")})
        else:
            return render(request, 'index.html', {"error_message": "用户名或密码错误"})    
        

    return render(request,'index.html')
    # return render(request,'welcome.html',{"username":request.POST.get("username")})

def user_logout(request):
    logout(request)
    return render(request,'index.html')

def register(request):
    # return render(request,'register.html')
    if request.method == 'GET':
        return render(request, 'register.html')
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if User.objects.filter(username=username):
            error_message = "用户名已存在"
            return render(request, 'register.html', {"error_message": error_message})
        elif password != password2:
            error_message = "两次密码不一致"
            return render(request, 'register.html', {"error_message": error_message})
        else:
            User.objects.create(username=username, password=make_password(password))
            request.session['username'] = username
            return render(request, 'register.html', {"success":True})
    
    return render(request, 'register.html')