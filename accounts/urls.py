from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from .views import AccountDeleteView 
from .views import CustomPasswordChangeView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', CustomPasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('account_delete/<int:pk>/', views.AccountDeleteView.as_view(), name='account_delete'),
    path('account_setting/', views.account_setting, name='account_setting'),
]