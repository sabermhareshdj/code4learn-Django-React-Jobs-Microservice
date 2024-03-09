from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager , PermissionsMixin

'''
** There are three ways to create a user
   this is from django 5 information store in databaseDjango 
              1- username   2- email  3 - password  4 - firstname   5 - lastname  ** and your are Admin or superUser .
- ono-to-one   : -->  if you want add image or any think -- connect profile user django : one-to-one
- abstractUser : fileds ---- > permission qroups auth views
                Use an class , do not use it directly . craete many of class Employee or calss Manager 
                (There are things in common between them) can use class Inherits from the this class without accessing it .
                class User : abstract

                class Employee(User):

                class Manager(User):

- abstractBaseUser : low level : Design everything according to system requirements. Freedom of design .
______________________________________________________________________________________________________________
what is manager :
products.objects.all() ==> objects : ( Inherits model Manager from django )

* When you study Django you build...
  - Queryset : bulid custom ----> It is not okay to be (Chained) غير مقيد
  - Model Manager : bulid custom ---> can Chained يمكن ان يكون مقيد
    (مثال 
    #products.objects.all().filter().orderby()
اي انها يمكن بناء اكثر من طريقة بعد الانتهاء من الاوله يتم تنفيذ الثانية و ثم الثالثة )

'''
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
    extra_fields.setdefault('is_staff',True)
    extra_fields.setdefault('is_superuser',True)
    return self.create_user(email,password,**extra_fields)



class CustomUser(AbstractUser,PermissionsMixin):
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
