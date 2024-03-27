from django.urls import path
from . import views



urlpatterns = [
  path('login/' , views.UserLoginAPI.as_view(),name='user-login'),
  path('signup/' , views.UserSignupAPI.as_view(),name='user-signup'),
  path('logout/' , views.UserLogoutAPI.as_view(),name='user-logout'),
  path('profile/' , views.UserProfile.as_view(),name='user-profile'),
  path('change-password/' , views.ChangePasswordAPI.as_view(),name='user-change'),
  path('resend-activation/' , views.ResendActiovationCodeAPI.as_view(),name='resend-activation-code'),
  path('reset-password/' , views.PasswordResetAPI.as_view(),name='user-reset'),

]