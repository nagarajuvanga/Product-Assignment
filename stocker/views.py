from django.shortcuts import render
from django.contrib import messages

from dispatcher.models import Dispatcher
from register.models import Stocker
from stocker.models import Product


def stocker_login(request):
    return render(request,"stocker/stocker_login.html")


def save_stocker_login(request):
    na = request.POST.get("sl1")
    passwo = request.POST.get("sl2")
    try:
        res = Stocker.objects.get(name=na, password=passwo)
        return render(request, "stocker/welcome_stocker.html", {"naga": res})
    except Stocker.DoesNotExist:
        return render(request, "stocker/stocker_login.html", {"error_message": "Invalid User"})


def change_password(request):
    return render(request,"stocker/change_password.html")


def new_password(request):
    old=request.POST.get("c1")
    new=request.POST.get("c2")
    conf=request.POST.get("c3")
    if new==conf:
        try:
            Stocker.objects.get(password=old)
            Stocker.objects.filter(password=old).update(password=new)
            return render(request,"stocker/welcome_stocker.html")
        except Stocker.DoesNotExist:
            messages.error(request,"Invalid User")
            return render(request,"stocker/change_password.html")
    else:
        print("invalid")


def product(request):
    res=Product.objects.all()
    return render(request,"stocker/product_details.html",{"data":res})


def add_product(request):
    pno=request.POST.get("p1")
    pname=request.POST.get("p2")
    pprice=request.POST.get("p3")
    pquantity=request.POST.get("p4")
    Product(product_no=pno, product_name=pname,product_price=pprice,product_quantity=pquantity).save()
    res=Product.objects.all()
    return render(request,"stocker/product_details.html",{"data":res})


def delete_product(request):
    return render(request,"stocker/delete_product.html")