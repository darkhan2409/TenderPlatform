from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Category


class CategoryApiView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

