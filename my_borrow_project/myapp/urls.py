from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'), 
    path('index',views.index,name = 'index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    
    path('logout/',  auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('borrow/<int:item_id>/form/', views.borrow_form, name='create_borrow_request'),
    path('user/status/', views.user_status, name='user_status'),
    path('request/cancel/<int:request_id>/', views.cancle_request, name='cancel_request'),
    path('user/', views.user, name='user'),
    # จัดการหมวดหมู่และสินค้า
    path('category/<int:category_id>/',views.item_by_category,name='item_by_category'),
    path('item/<int:item_id>/', views.item_detail ,name='item_detail')

]
