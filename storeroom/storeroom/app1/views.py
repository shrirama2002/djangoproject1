from django.shortcuts import render, redirect
#import below packages
from app1.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.
#register view creation
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 == pass2:
            user = User.objects.create_user(name, email, pass1)
            user.is_User = True
            user.save()
            messages.success(request, "Registered Successfully")
            return render(request, "login.html")
        return redirect("register")
    return render(request, "register.html")

def register_Vendor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 == pass2:
            user = User.objects.create_user(name, email, pass1)
            user.is_Vendor = True
            user.save()
            messages.success(request, "Registered Successfully")
            return render(request, "login.html")
        return redirect("register")
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(request, username=name, password=password)
        login(request,user)
        if user is not None:
            if user.is_User:
                return render(request, "home.html")
            elif user.is_admin: #and user.is_Vendor:
                return render(request, "homea.html")
            elif user.is_Vendor and not(user.is_admin):
                return render(request,"homes.html")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

