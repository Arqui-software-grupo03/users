from .renderers import UserJSONRenderer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import User
from .serializers import (LoginSerializer, RegistrationSerializer, UserSerializer, ProfileSerializer,
    DeactivateSerializer)
from django.core.exceptions import ObjectDoesNotExist


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):

        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        print(serializer_data)

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveAPIView(RetrieveAPIView):

    #queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = ProfileSerializer

    def retrieve(self, request, *args, **kwargs):


        try:
            user = User.objects.get(pk=self.kwargs['user'])
            print(user.is_active)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            content = {'error': 'not found'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        #else:
        #    content = {'user': 'not found'}
        #    return Response(content, status=status.HTTP_404_NOT_FOUND)



class AllUserRetrieveAPIView(ListAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    #renderer_classes = (UserJSONRenderer,)
    serializer_class = ProfileSerializer


class DeactivateUserAPIView(UpdateAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = DeactivateSerializer

    def update(self, request, *args, **kwargs):
        serializer_data = {'is_active': 0}

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=False)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

