from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('form',views.form),
    path('user',views.user)
]
