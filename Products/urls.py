# from django.contrib import admin
from django.urls import path,include
from Products import views

urlpatterns = [
    

    path("",views.productindex,name='products')

    
]

