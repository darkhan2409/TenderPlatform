from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer


class CompanyApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        data = Company.objects.all()
        serializer = CompanySerializer(instance=data, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)


class CompanyUpdateApiView(APIView):
    permission_classes = [IsAdminUser, ]

    def patch(self, request, about_id):  # проконсультироваться
        company = Company.objects.get(id=about_id)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = CompanySerializer(company).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

