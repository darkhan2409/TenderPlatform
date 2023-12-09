from rest_framework.serializers import ModelSerializer
from .models import *


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['title', 'username', 'password', 'email', 'bin', 'phone']

    def create(self, validated_data):
        supplier = Supplier.objects.create(**validated_data)
        supplier.set_password(validated_data['password'])
        supplier.save()
        return supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['title', 'username', 'email', 'bin', 'phone']


class SupplierUpdateSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['title', 'email', 'phone']


