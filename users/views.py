from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.model import User
from users.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
