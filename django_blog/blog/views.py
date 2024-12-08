"ListView", "DetailView", "CreateView", "UpdateView", "DeleteView"
["CommentCreateView", "CommentUpdateView", "LoginRequiredMixin", "UserPassesTestMixin", "CommentDeleteView"]
["Post.objects.filter", "title__icontains", "tags__name__icontains", "content__icontains"]
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
