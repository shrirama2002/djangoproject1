from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #add all endpoints like register,
    path("register/",views.register,name="register"),
    path("register_Vendor/",views.register_Vendor,name="register_V"),
    path("login/",views.user_login,name="login"),

]