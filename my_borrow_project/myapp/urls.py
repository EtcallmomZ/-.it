from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index),
    path('log_in',views.log_in),
    path('form',views.form)
]
