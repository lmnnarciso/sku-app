from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from django.http import JsonResponse

from core.models import Supplier, ProductSupplier
from supplier import serializers


class SupplierListView(APIView):
    # serializer_class = serializers.ProductCategorySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        supplier = request.data
        # print(product_category)
        serializer = serializers.SupplierSerializer(data=supplier)
        if serializer.is_valid(raise_exception=True):
            # print('aweaee')
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        
        supplier = Supplier.objects.all()
        serializer = serializers.SupplierSerializer(data=supplier, many=True)
        serializer.is_valid()

        return Response(serializer.data, status=200)

class ProductSupplierListView(APIView):
    # serializer_class = serializers.ProductCategorySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        product_supplier = request.data
        # print(product_category)
        serializer = serializers.ProductSupplierSerializer(data=product_supplier)
        if serializer.is_valid(raise_exception=True):
            # print('aweaee')
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        
        product_supplier = ProductSupplier.objects.all()
        serializer = serializers.ProductSupplierSerializer(data=product_supplier, many=True)
        serializer.is_valid()

        return Response(serializer.data, status=200)