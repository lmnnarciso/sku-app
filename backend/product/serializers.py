from rest_framework import serializers

from core.models import Product, ProductCategory


class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description')
        
    def create(self, validated_data):
        """
        Create and return a new `Product Category` instance, given the validated data.
        """
        # print(validated_data)
        return ProductCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product Category` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    # def patch(self, instance, validated_data):

    
class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    product_category_id = serializers.IntegerField()
    unit_price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'product_category_id', 'unit_price', 'quantity']
        # order_by = ['-name']

    def create(self, validated_data):
        """
        Create and return a new `Product` instance, given the validated data.
        """
        # validated_data['migz'] = 'migs'
        # print(validated_data)
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.product_category = validated_data.get('product_category_id', instance.product_category)
        instance.unit_price = validated_data.get('unit_price', instance.unit_price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

