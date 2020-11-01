from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('usersignup/', views.usersignup, name='usersignup'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('expedition/', include('proxima_exped.urls')),
]
