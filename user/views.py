from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import \
    LoginView, LogoutView, logout_then_login, redirect_to_login, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView


from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'user/home.html')


'''
------------------ AUTHENTICATION ----------------------
--------------------------------------------------------

########## usable function for login and logout 
    1 - login(request)
    2 - logout(request)
    3 - authenticate(request) :
        - If the given credentials are valid, return a User object.

    4 - logout_then_login(login_url) : 
        - Log out the user if they are logged in. Then redirect to the login page.
        - use settings.LOGIN_URL of login_url

    5 - redirect_to_login(login_url) : 
        - Redirect the user to the login page, passing the given 'next' page.
###############################################


## 1 - LoginView :
        attrs :
            - form_class = AuthenticationForm
            - authentication_form = None
            - next_page = None
            - redirect_field_name = REDIRECT_FIELD_NAME
            - template_name = "registration/login.html"
            - redirect_authenticated_user = False
            - extra_context = None
        methods:
            - get_success_url
            - get_redirect_url
            - form_valid
            - get_default_redirect_url

    ---> use function <login(request, user)> to login in <form_valid> method
    ---> use settings.LOGIN_REDIRECT_URL in <get_default_redirect_url>
##################

## 2 - LogoutView :
        attrs:
            - next_page = None
            - redirect_field_name = REDIRECT_FIELD_NAME
            - template_name = "registration/logged_out.html"
            - extra_context = None
        methods:
            - get_next_page
            - get_context_data
    ---> use settings.LOGOUT_REDIRECT_URL in <get_next_page>

##################
'''

class CustomLoginView(LoginView):
    template_name = 'user/login.html' # default: "registration/login.html"
    redirect_authenticated_user = True # redirect to get_success_url(self)

    # define the default url in setting.LOGIN_REDIRECT_URL
    # def get_success_url(self):
    #     return reverse_lazy('user:profile')

class CustomLogoutView(LogoutView):
    next_page = 'user:home'





'''
------------------------- REGISTRATION -------------------------
----------------------------------------------------------------

#### for registration purpose never view is given.
#### but exist all required form for managing views (forms.py)

----------------------------------------------------------------
----------------------------------------------------------------
'''


class Signup(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'

    # for redirect authenticated user
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("user:profile")
        return super(Signup, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('user:profile')

class ChangeInfo(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user/update.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user:profile')



'''
------------------------- RESET PASSWORD -------------------------
------------------------------------------------------------------

# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks the link the user clicked and
#   prompts for a new password
# - PasswordResetCompleteView shows a success message for the above

## 1 - PasswordChangeView
## 2 - PasswordChangeDoneView
------------------------------------------------------------------
------------------------------------------------------------------
'''


class ResetPass(PasswordChangeView):
    template_name = 'user/reset_pass.html'     
    success_url = reverse_lazy("user:change_done")

class PassChangeDone(PasswordChangeDoneView):
    template_name = 'user/pass_change_done.html'

    def dispatch(self, request, *args, **kwargs):
        # logout(request)
        return super().dispatch(request, *args, **kwargs)
    
    

@login_required(login_url='user:login')
def profile(request):
    return render(request, 'user/profile.html')