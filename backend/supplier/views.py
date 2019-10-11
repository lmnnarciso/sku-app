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


class SupplierDetailView(APIView):

    def get_object(self, pk):
        # print(pk)
        try:
            return Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        supplier = self.get_object(pk)

        data = Supplier.objects.filter(id=supplier.id).values()[0]
        serializer = serializers.SupplierSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        supplier = self.get_object(pk=kwargs['pk'])

        serializer = serializers.SupplierSerializer(supplier,
                                                    data=request.data, 
                                                    partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(data="wrong parameters", code=400)

    def delete(self, request, pk, format=None):
        supplier = self.get_object(pk)
        supplier.delete()
        return Response(status=204)

        
    def put(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = serializers.ProductCategorySerializer(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
