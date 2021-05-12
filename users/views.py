from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from users.model import User
from users.serializers import RegisterSerializer, UserSerializer


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'id'

    @action(
        methods=('get', 'patch'),
        detail=False,
        permission_classes=(IsAuthenticated,)
    )
    def me(self, request):
        user_profile = get_object_or_404(
            User,
            id=request.user.id
        )
        if request.method == 'GET':
            serializer = UserSerializer(user_profile)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        serializer = UserSerializer(
            user_profile,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(
            role=user_profile.role,
            avatar=user_profile.avatar,
            bio=user_profile.bio,
            program_language=user_profile.program_language)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
