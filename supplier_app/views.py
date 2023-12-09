from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout, authenticate

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SignUpApiView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):  # create (registration)
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignIn(APIView):  # authenticate
    permission_classes = [AllowAny, ]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {'message': 'Welcome!'}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'message': 'Username or/and Password is not valid!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class SignOut(APIView):  # exit
    def get(self, request):
        logout(request)
        return Response({'message': 'You logged out successfully'}, status=status.HTTP_200_OK)


class SupplierProfile(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):  # read
        data = SupplierSerializer(request.user).data
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):  # delete
        user = request.user
        user.delete()
        return Response({'message': 'Supplier is deleted!'}, status=status.HTTP_200_OK)

    def patch(self, request):  # update
        user = request.user
        serializer = SupplierUpdateSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = SupplierSerializer(user).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
