from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model  # get user from settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .serializers import UserSerializer


User = get_user_model()  # CustomsUser 

class UserLoginAPI(ObtainAuthToken):
  
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=status.HTTP_200_OK)



class UserLogoutAPI(APIView):
  permission_classes = [IsAuthenticated]

  def post(self, request, *args, **kwargs):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


class ChangePasswordAPI(APIView):
  permission_classes = [IsAuthenticated]

  def put(self,request):
    user = request.user #
    data = request.data

    if not user.check_password(data.get('old_password')):
      return Response({'old_password':'Wrong Password'},status=status.HTTP_400_BAD_REQUEST)

    # update password for user 
    user.set_password(data.get['new_password'])
    user.save()
    return Response({'message':'Password Was Changed Successfully'},status=status.HTTP_200_OK)


class ResendActiovationCodeAPI(APIView):

  def post(self,request,*args, **kwargs):
    email = request.data.get('email')
    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      return Response({'error':'User with this email does not exist'},status=status.HTTP_404_NOT_FOUND)

    if user.is_active:
      return Response({'error':'this user is already activate'},status=status.HTTP_400_BAD_REQUEST)

    # create activation link 
    current_site = get_current_site(request)   #get domain : url 
    mail_subject = 'Activate Your Account'
    message = render_to_string('accounts/activation_email.html',{
      'user' : user ,
      'domain' : current_site.domain ,
      'uid' : urlsafe_base64_decode(force_bytes(user.id)) ,
      'token' : default_token_generator.make_token(user)

    })
    to_email = user.email
    send_mail(mail_subject,message,'saber.mharsh@gmail.com',[to_email])
    return Response({'success':'Activation email has been sent'}, status=status.HTTP_200_OK)







class PasswordResetAPI(APIView):
    def post(self,request,*args, **kwargs):
      email = request.data.get('email')
      try:
        user = User.objects.get(email=email)
      except User.DoesNotExist:
        return Response({'error':'User with this email does not exist'},status=status.HTTP_404_NOT_FOUND)
      if user.is_active:
        return Response({'error':'this user is already activate '},status=status.HTTP_400_BAD_REQUEST)

      # create activation link 
      current_site = get_current_site(request)   #get domain : url 
      mail_subject = 'Reset Your Account'
      message = render_to_string('accounts/password_reset_email.html',{
        'user' : user ,
        'domain' : current_site.domain ,
        'uid' : urlsafe_base64_decode(force_bytes(user.id)) ,
        'token' : default_token_generator.make_token(user)

      })
      to_email = user.email
      send_mail(mail_subject,message,'saber.mharsh@gmail.com',[to_email])
      return Response({'success':'Activation email has been sent'}, status=status.HTTP_200_OK)
 


class UserSignupAPI(APIView):
  def post(self,request,*args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      user =serializer.save()
      user.is_active = False
      user.save()

      # create activation link 
      current_site = get_current_site(request)   #get domain : url 
      mail_subject = 'Activate Your Account'
      message = render_to_string('accounts/activation_email.html',{
        'user' : user ,
        'domain' : current_site.domain ,
        'uid' : urlsafe_base64_decode(force_bytes(user.id)) ,
        'token' : default_token_generator.make_token(user)

      })
      to_email = user.email
      send_mail(mail_subject,message,'saber.mharsh@gmail.com',[to_email])
      return Response({'success':'User registered successfuly , plase check your email to activate your account '}, status=status.HTTP_201_CREATED)
    return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class UserProfile(APIView):
  def get(self,request,*args, **kwargs):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data , status=status.HTTP_200_OK)
