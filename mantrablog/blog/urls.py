"""mantrablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home,signup,loginn,create,alllist,viewbyid,logoutt,like_comment,send_email,yourlist

urlpatterns = [
    path('', home,name='home'),
    path('signup/', signup,name='singup'), 
    path('login/', loginn,name='login'), 
    path('create/', create,name='create'), 
    path('alllist/', alllist,name='alllist'), 
    path('list/', yourlist,name='yourlist'), 
    path('viewbyid/<id>', viewbyid,name='viewbyid'), 
    path('logout/', logoutt,name='logoutt'), 
    path('toggle_comment_like/<id>/',like_comment ,name='like'), 
    path('send_email/', send_email, name='send_email'),

    
]
