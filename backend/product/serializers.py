from rest_framework import serializers

from core.models import Product, ProductCategory, ProductSupplier, ProductStockLevel


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


class ProductSupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    product_id = serializers.UUIDField()
    supplier_id = serializers.IntegerField()
    date_to_supply = serializers.DateTimeField()
    quantity_supply = serializers.IntegerField()
    price = serializers.IntegerField()

    class Meta:
        model = ProductSupplier
        fields = ('id', 'product_id', 'supplier_id', 'date_to_supply', 'quantity_supply', 'price')
        
    def create(self, validated_data):
        """
        Create and return a new `Supplier` instance, given the validated data.
        """
        # print(validated_data)
        return ProductSupplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Supplier` instance, given the validated data.
        """
        # instance.name = validated_data.get('name', instance.name)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.supplier_id = validated_data.get('supplier_id', instance.supplier_id)
        instance.date_to_supply = validated_data.get('date_to_supply', instance.date_to_supply)
        instance.quantity_supply = validated_data.get('quantity_supply', instance.quantity_supply)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductStockLevelSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    quantity_level = serializers.IntegerField()
    product_id = serializers.UUIDField()
    product_restocking = serializers.DateTimeField()
    
    class Meta:
        model = ProductStockLevel
        fields = ['id', 'quantity_level', 'product_id', 'product_restocking']
        # order_by = ['-name']

    def create(self, validated_data):
        """
        Create and return a new `Product Stock Level` instance, given the validated data.
        """
        # validated_data['migz'] = 'migs'
        # print(validated_data)
        return ProductStockLevel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Product` instance, given the validated data.
        """
        instance.quantity_level = validated_data.get('quantity_level', instance.quantity_level)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.product_restocking = validated_data.get('product_restocking', instance.product_restocking)
        instance.save()
        return instance