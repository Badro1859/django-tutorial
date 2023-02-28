
from django.contrib.auth.forms import \
    AuthenticationForm, \
    UserCreationForm, UserChangeForm, \
    SetPasswordForm, PasswordChangeForm, PasswordResetForm


'''
------------------------- AUTHENTICATION -------------------------
------------------------------------------------------------------
## AuthenticationForm :
    fields:
        - username
        - password
    methods:
        - get_user


------------------------- REGISTRATION -------------------------
----------------------------------------------------------------
## 1 - UserCreationForm :
    fields:
        - username
        - password1
        - password2
########################

## 2 - UserChangeForm : 
    fields:
        - __all__ (of the User model)
        - password : ReadOnlyPasswordHashField
########################

------------------------- RESET PASSWORD -----------------------
----------------------------------------------------------------
## 1 - SetPasswordForm(user):
    fields:
        - new_password1
        - new_password2
############################

## 2 - PasswordChangeForm(user):
    fields:
        - old_password
        - new_password1
        - new_password2
############################

## 3 - PasswordResetForm:
    fields:
        - email
    --> reset password with send email to user
############################

## 4 - AdminPasswordChangeForm :
    - A form used to change the password of a user in the admin interface.
############################


'''