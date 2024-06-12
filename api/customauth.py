from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class Customauthcation(BaseAuthentication):
    def authenticate(self, request):
        username=request.GET.get('username')
        if username is None:
            return None
        
        try:
            user=User.object.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('no Such Match')
        return (User,None)
    
        