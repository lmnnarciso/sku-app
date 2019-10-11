from rest_framework import serializers

from core.models import Supplier


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
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


