from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
  pass

class PasswordResetAPI(APIView):
  pass 


class UserSignupAPI(APIView):
  pass

class UserProfile(APIView):
  pass