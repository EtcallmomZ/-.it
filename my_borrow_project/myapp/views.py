from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")

def form(request):
    return render(request,"form.html")

def user(request):
    return render(request,"user.html")
