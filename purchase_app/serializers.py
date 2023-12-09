from rest_framework.serializers import ModelSerializer, DateTimeField
from .models import Purchase
from category_app.serializers import CategorySerializer
from status_app.serializers import StatusSerializer


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['title', 'category', 'closing_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation


class PurchaseDetailSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['status'] = StatusSerializer(instance.status).data
        representation['category'] = CategorySerializer(instance.category).data
        return representation

    opening_date = DateTimeField(format="%Y-%m-%d, %H:%M")
    closing_date = DateTimeField(format="%Y-%m-%d, %H:%M")
