from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from .serializers import StatusSerializer
from rest_framework.response import Response
from rest_framework import status


class StatusApiView(APIView):
    permission_classes = [IsAdminUser, ]

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

