from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from django.contrib import auth
from django.contrib.auth.models import User



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    number=models.IntegerField(default=0,blank=True)
    role=models.CharField(max_length=30,blank=True)
    can_play = models.BooleanField(default=False)
    is_alive = models.BooleanField(default=False,blank=True)
    group=models.CharField(max_length=30,blank=True)
    has_lynched=models.BooleanField(default=False,blank=True)
    side=models.CharField(max_length=30,blank=True)
    message=models.CharField(max_length=100,blank=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    # def get_username(self):
    #     return self.username


    def __str__(self):
        return self.username

#For making list of alive people
# def get_user(request,x,m):
#     try:
#         return CustomUser.objects.filter(is_alive=True,number=x,group=m).get()
#     except CustomUser.DoesNotExist:
#         return None
# #or this:
# def get_user2(request,x,m):
#     if CustomUser.objects.filter(is_alive=True,group=m,number=x).exists():
#         return CustomUser.objects.get(is_alive=True,group=m,number=x)


#For assigning roles at start
def set_user_role(request,y,x):
    try:
        return CustomUser.objects.filter(number=y,group=request.user.group).update(role=x)
    except CustomUser.DoesNotExist:
        return None


def get_user(request,x):
    try:
        return CustomUser.objects.filter(is_alive=True,number=x,group=request.user.group).get()
    except CustomUser.DoesNotExist:
        return None
#or this:
def get_user2(request,x):
    if CustomUser.objects.filter(is_alive=True,group=request.user.group,number=x).exists():
        return CustomUser.objects.get(is_alive=True,group=m,number=x)
    