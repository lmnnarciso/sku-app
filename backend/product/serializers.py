from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ['name', 'description', 'product_category', 'unit_price', 'quantity']