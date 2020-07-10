from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from dispatcher.models import Dispatcher
from register.models import Stocker


def adminshowLogin(request):
    return render(request,"register/login.html")


def save_login(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    if un == "nagaraju" and pa == "nagaraju":
        return render(request, "register/welcome_page.html")
    else:
        messages.error(request, "Invalid User")
        return render(request,"register/login.html")


def add_stocker(request):
    res=Stocker.objects.all()
    return render(request,"register/add_stocker.html",{"data":res})


def save_stocker(request):
    no=request.POST.get("s1")
    na=request.POST.get("s2")
    con=request.POST.get("s3")
    pas=request.POST.get("s4")
    result=Stocker(idno=no,name=na,contact=con,password=pas).save()
    result=Stocker.objects.all()
    return render(request, "register/add_stocker.html",{"data":result})


def delete_stoker(request):
    no = request.POST.get("t1")
    results= Stocker.objects.get(idno=no).delete()
    results=Stocker.objects.all()
    return render(request, "register/add_stocker.html",{"data":results})


def mr_nagaraju(request):
    return render(request,"register/welcome_page.html")


def add_dispatcher(request):
    result = Dispatcher.objects.all()
    return render(request,"register/add_dispatcher.html",{"data":result})


def save_dispatcher(request):
    no = request.POST.get("d1")
    na = request.POST.get("d2")
    con = request.POST.get("d3")
    pas = request.POST.get("d4")
    result = Dispatcher(idno=no, name=na, contact=con, password=pas).save()
    result = Dispatcher.objects.all()
    return render(request, "register/add_dispatcher.html",{"data": result})


def delete_dispatcher(request):
    no = request.POST.get("t1")
    results = Dispatcher.objects.get(idno=no).delete()
    results = Dispatcher.objects.all()
    return render(request, "register/add_dispatcher.html",{"data": results})

