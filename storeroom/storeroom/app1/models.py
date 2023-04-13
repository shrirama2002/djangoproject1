from django.db import models
from django.contrib.auth.models import AbstractUser
#here im creating user,admin and vendor distinctions for login

# Create your models here.
class User(AbstractUser):
    is_User = models.BooleanField('is_User',default=False)
    is_admin = models.BooleanField('is_admin',default=False)
    is_Vendor = models.BooleanField('is_Vendor',default=False)

    def save(self, *args, **kwargs):
        if self.is_superuser and not self.is_admin:
            self.is_admin = True
            self.is_Vendor = True
        super().save(*args, **kwargs)