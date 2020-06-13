from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
# from django.contrib.auth.models import User


from User.models import Post
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    if request.method=="POST":
        text=request.POST.get('text')
        
        post= Post(id=None ,user=request.user,text=text,created_at=datetime.today(),updated_at=datetime.today())        
        post.save()
        messages.success(request, 'Your Post has been sent!!')

    return render(request,'index.html')


def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')


    return render(request,'login.html')


    return render(request,'login.html')



def logoutUser(request):
    logout(request)
    return redirect('/login')