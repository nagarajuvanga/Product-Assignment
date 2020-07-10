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
from stocker import views

urlpatterns = [
    #path('admin_login/',views.adminshowLogin,name="admin_login"),
    path('stocker_login/',views.stocker_login,name="stocker_login"),
    path('save_stocker_login/',views.save_stocker_login,name="save_stocker_login"),
    path('change_password/',views.change_password,name="change_password"),
    path('new_password/',views.new_password,name="new_password"),
    path('product/',views.product,name="product"),
    path('add_product/',views.add_product,name="add_product"),
    path('delete_product/',views.delete_product,name="delete_product")

]
