from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import *
from .serializers import *


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = User.objects.get(id=user.id)
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
        })


def delete(self, request, pk, format=None):
    user_delete = User.objects.filter(pk)
    user_delete.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


def put(self, request, pk, format=None):
    editing_user = User.objects(pk)
    serializer = UserSerializer(editing_user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        return Response(UserSerializer(request.user,).data)
