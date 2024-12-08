"post/<int:pk>/delete/", "post/<int:pk>/update/", "post/new/"

from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('login', views.login_user, name='login')
    
]
