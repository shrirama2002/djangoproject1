from django.contrib import admin

# Register your models here.
from app1.models import User
# Here im registering my models that i have created in the models.py
# my app name is app1 so from app1.models 
# i have used only User class so importing User model
admin.site.register(User)
# i have registered my model