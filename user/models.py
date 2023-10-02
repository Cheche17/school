
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User

# class Userprofile(models.Model):
#      user = models.ForeignKey(UserAccount, related_name='useraccount', on_delete=models.CASCADE)
    
    
class UserManager(BaseUserManager):
    
    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email Required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Super user is not successful'
            )
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Super user must be superuser'
            )
        
        return self._create_user(email, password, **extra_fields)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField('firtname', max_length=255, blank=True)
    lastname = models.CharField('lastname', max_length=255, blank=True)
    email = models.EmailField(unique=True, max_length=255, blank=False)
    phone = models.CharField('phone', max_length=255, blank=True)
    password1 = models.CharField('password', max_length=255, blank=True)
    password2 = models.CharField('confirm', max_length=255, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=False)
    is_supseruser = models.BooleanField('super user', default=False)
    date_joined = models.DateTimeField('date joined',default=timezone.now)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    def __str__(self):
        return self.email

    def full_name(self):
        return self.firstname+""+self.lastname
    