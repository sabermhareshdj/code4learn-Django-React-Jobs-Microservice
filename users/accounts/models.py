from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager , PermissionsMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
  def create_user(self,email,password=None,**extra_fields):
    if not email :
      raise ValueError('The Email Field is Required')
    email = self.normalize_email(email)
    
    user = self.model(email=email , **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self,email,password=None,**extra_fields):
    print('in createsuperuser ...')
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_superuser',True)
    extra_fields.setdefault('is_active',True)

    return self.create_user(email,password,**extra_fields)



class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(unique=True) # login with email
  username = models.CharField(max_length=25 , null=True , blank=True) # It is best that the name be added and be unique
  is_active = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True) # It does not appear in the admin panel

  #user manager
  objects = CustomUserManager()

  USERNAME_FIELD = 'email' # login 
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email
