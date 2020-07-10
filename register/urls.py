"""Project1_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from register import views

urlpatterns = [
    path('login/',views.adminshowLogin,name="register_login"),
    path('save_login/',views.save_login,name="save_login"),
    path('add_stocker/',views.add_stocker,name="add_stocker"),
    path('save_stocker/',views.save_stocker,name="save_stocker"),
    path('delete_stoker/',views.delete_stoker,name="delete_stoker"),
    path('mr_nagaraju/',views.mr_nagaraju,name="mr_nagaraju"),
    path('add_dispatcher/',views.add_dispatcher,name="add_dispatcher"),
    path('save_dispatcher/',views.save_dispatcher,name="save_dispatcher"),
    path('delete_dispatcher/',views.delete_dispatcher,name="delete_dispatcher")

]
