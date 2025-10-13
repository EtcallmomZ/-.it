from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")

def form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,"form.html" , {'form' : form})

def user(request):
    return render(request,"user.html")
