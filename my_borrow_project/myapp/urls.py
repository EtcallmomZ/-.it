from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('index',views.index,name = 'index'),
    path('login',views.login_view, name = 'login'),
    path('signup',views.signup, name = 'signup'),
    path('user',views.user,name = 'user')
]
