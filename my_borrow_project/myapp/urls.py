from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('index',views.index,name = 'index'),
    path('login', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),

    path('borrow/<int:item_id>/form/', views.created_borrow_request, name='create_borrow_request'),
    path('user/status/', views.user_status, name='user_status'),
    path('request/cancel/<int:request_id>/', views.cancle_request, name='cancel_request'),

    path('user/', views.user, name='user')

]