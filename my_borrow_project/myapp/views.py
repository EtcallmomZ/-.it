from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = " eiweiw "
    age = 18
    return render(request,"index.html",{"name":name,"age":age})
def login(request):
    return render(request,"login.html")

def form(request):
    return render(request,"form.html")

def user(request):
    return render(request,"user.html")
