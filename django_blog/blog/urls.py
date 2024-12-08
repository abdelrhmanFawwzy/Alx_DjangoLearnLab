"post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"
["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]
from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('login', views.login_user, name='login')
    
]
