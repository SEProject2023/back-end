from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method == "POST":
        print(request.POST.get("username"))
        print(request.POST.get("password"))
    # return render(request,'index.html')
    return render(request,'welcome.html',{"username":request.POST.get("username")})