from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class PurchaseApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        if request.user.is_authenticated:
            purchase = Purchase.objects.all()
            data = PurchaseDetailSerializer(purchase, many=True).data
            return Response(data, status=status.HTTP_200_OK)
        else:
            purchase = Purchase.objects.all()
            data = PurchaseSerializer(purchase, many=True).data
            return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.user.is_staff:
            serializer = PurchaseDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


