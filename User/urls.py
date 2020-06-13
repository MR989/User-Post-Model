# from django.contrib import admin
from django.urls import path,include
from User import views

urlpatterns = [
    

    path("",views.index,name='user'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),

    
]

