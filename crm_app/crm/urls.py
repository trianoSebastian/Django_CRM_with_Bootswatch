from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name='home'),
    path('register', views.register,name='register'),
    path('login', views.login_user,name='login'),
    path('user_logout', views.user_logout,name='user_logout'),
    #CRUD
    path('dashboard', views.dashboard,name='dashboard'),
    path('create_record', views.create_record,name='create_record'),
    path('update_record/<int:pk>', views.update_record,name='update_record'),
    path('record/<int:pk>', views.view_record,name='view_record'),
    path('delete/<int:pk>', views.delete_record,name='delete_record'),
]
