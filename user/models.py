from django.db import models

# Create your models here.

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager # root of Users classes
from django.contrib.auth.models import User, AbstractUser, UserManager, PermissionsMixin # ***

#### usable package in them
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)


'''
########### Build-in model for authentication and permission


## 1 - <AbstractBaseUser> 
        fields : 
            - password
            - last_login
        property :
            - is_authenticated
            - is_anonymous
            - ...
        methods:
            - set_password
            - get_email_field_name
            - ...

    --> this model use attrs :
        - REQUIRED_FIELDS
        - USERNAME_FIELD
        - EMAIL_FIELD
################################

## 2 - <AbstractUser> (AbstractBaseUser, PermissionsMixin)
        fields:
            - username
            - email
            - is_staff
            - ...
        methods:
            - email_user
            - ...
        
    --> this model use <UserManager>
################################


## 3 - User (AbstractUser) :  Users within the Django authentication system are represented by this
    model.  
###############################


## 4 - <PermissionsMixin>
        fields:
            - is_superuser
            - groups
            - user_permissions
        methods:
            - get_user_permissions(obj=None)
            - get_group_permissions
            - has_perm(perm)
            - has_perms(perm_list)
    
    --> permission = <app_name>.<model_name>.<create, update, delete, retreive>
##############################


'''