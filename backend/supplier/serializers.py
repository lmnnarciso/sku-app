from rest_framework import serializers

from core.models import Supplier, Product, ProductSupplier


class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email = serializers.EmailField()
    name = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Supplier
        fields = ('id', 'email', 'name', 'address')
        
    def create(self, validated_data):
        """
        Create and return a new `Supplier` instance, given the validated data.
        """
        # print(validated_data)
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Supplier` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.description)
        instance.save()
        return instance


class ProductSupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    product_id = serializers.IntegerField()
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
