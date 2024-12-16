["ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . forms import *




# Create your views here.

def home(request):
    return render(request, 'blog/base.html', {} )


def login_user(request):
    form = login_user_form()
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'authentcation/login.html', {'form':form} )
    
    
def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')
        else:
            return redirect('register')
            
    else:
        form = UserCreationForm()
        return render(request, 'authentcation/register.html', {'form':form})
    
