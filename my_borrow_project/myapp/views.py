from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignUpForm # import signup มา
#import autencation form มาอันนี้ django ให้มาเป็นฟอร์มสำเร็จ
from django.contrib.auth.forms import AuthenticationForm 
#import การใช้งานพร้อมเปลี่ยนชื่อไม่ให้มันซ้ำกันเดี๋ยวทำงานไม่ได้
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout 
from .models import Item  # เราไป import Item มาจากไฟล์ models เพื่อมาเรียกใช้งาน



# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request,"index.html",context)

  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request, f"Welcome back ,{username}")
                return redirect('user')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request,"login.html", {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, "signup.html", {'form': form})


def user(request):
    return render(request,"user.html")
