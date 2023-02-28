
from django.urls import path

from user import views

app_name='user'
urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.Signup.as_view(), name='register'),
    
    path('profile/', views.profile, name='profile'),
    path('update/', views.ChangeInfo.as_view(), name='update'),
    path('reset-password/', views.ResetPass.as_view(), name='reset-pass'),
    path('reset-password-done/', views.PassChangeDone.as_view(), name='change_done'),
]
