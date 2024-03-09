from django.urls import path
from .views import UserLoginAPI , UserLogoutAPI , ChangePasswordAPI , UserSignupAPI , PasswordResetAPI



urlpatterns = [
  path('login/' , UserLoginAPI.as_view(),name='user-login'),
  path('signup/' , UserSignupAPI.as_view(),name='user-signup'),
  path('logout/' , UserLogoutAPI.as_view(),name='user-logout'),
  path('change-password/' , ChangePasswordAPI.as_view(),name='user-change'),
    path('reset-password/' , PasswordResetAPI.as_view(),name='user-reset'),

  




]