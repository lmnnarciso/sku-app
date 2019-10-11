from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, DestroyModelMixin

from django.http import JsonResponse, HttpResponse

from core.models import ProductCategory, Product, ProductSupplier, Supplier, ProductStockLevel
from product import serializers


class ProductCategoryListView(APIView):
    serializer_class = serializers.ProductCategorySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        product_category = request.data.get('product_category')
        serializer = serializers.ProductCategorySerializer(data=product_category)
        
        if serializer.is_valid(raise_exception=True):
            product_category_saved = serializer.save()
        return Response({"success": "Product Category '{}' created successfully".format(product_category_saved.name)})

    def get(self, request):
        product_category = list(ProductCategory.objects.values())
        serializer = serializers.ProductCategorySerializer(data=product_category, many=True)
        
        
        # print(product_category.id)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class ProductCategoryDetailView(APIView, UpdateModelMixin):
    # serializer_class = serializers.ProductCategorySerializer

    def get_object(self, pk):
        # print(pk)
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        product_category = self.get_object(pk)

        data = ProductCategory.objects.filter(id=product_category.id).values()[0]
        serializer = serializers.ProductCategorySerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        product_category = self.get_object(pk=kwargs['pk'])
        # print(request)
        # print(product_category.objects.values())
        # data = ProductCategory.objects.filter(id=product_category.id).values()[0]
        # print(kwargs['pk'])
        serializer = serializers.ProductCategorySerializer(product_category,
                                                            data=request.data, 
                                                            partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(data="wrong parameters", code=400)

    def delete(self, request, pk, format=None):
        product_category = self.get_object(pk)
        product_category.delete()
        return Response(status=204)

        
    def put(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = serializers.ProductCategorySerializer(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



class ProductView(APIView):
    """for Product API requests"""
    # serializer_class = serializers.ProductSerializer

    def get_queryset(self): #this method is called inside of get
        queryset = self.queryset.filter()
        return queryset

    def post(self, request, format=None):
        product = request.data
        serializer = serializers.ProductSerializer(data=product)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # print(serializer.data)
            return JsonResponse(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)

    def get(self, request):
        product = Product.objects.all()
        serializer = serializers.ProductSerializer(data=product, many=False)
        serializer.is_valid()
        # print(serializer)
        return JsonResponse(serializer.data, safe=False)

    



class ProductDetailView(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         raise Http404

    # def get_queryset(self): #this method is called inside of get
    #     queryset = self.queryset.filter()
    #     return queryset

    def get_object(self, pk):
        # print(pk)
        try:
            return Product.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)

        data = Product.objects.filter(id=product.id).values()[0]
        serializer = serializers.ProductSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        product = self.get_object(pk=kwargs['pk'])
        serializer = serializers.ProductSerializer(product,
                                                            data=request.data, 
                                                            partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(data="wrong parameters", code=400)

    def delete(self, request, pk, format=None):
        product_category = self.get_object(pk)
        product_category.delete()
        return Response(status=204)

        
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class ProductSupplierDetailView(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         raise Http404

    # def get_queryset(self): #this method is called inside of get
    #     queryset = self.queryset.filter()
    #     return queryset

    def get_object(self, pk):
        # print(pk)
        try:
            return ProductSupplier.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        product_supplier = self.get_object(pk)

        data = ProductSupplier.objects.filter(id=product_supplier.id).values()[0]
        serializer = serializers.ProductSupplierSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        product_supplier = self.get_object(pk=kwargs['pk'])
        serializer = serializers.ProductSupplierSerializer(product_supplier,
                                                            data=request.data, 
                                                            partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(data="wrong parameters", code=400)

    def delete(self, request, pk, format=None):
        product_supplier = self.get_object(pk)
        product_supplier.delete()
        return Response(status=204)

        
    def put(self, request, pk, format=None):
        product_supplier = self.get_object(pk)
        serializer = serializers.ProductSupplierSerializer(product_supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductStockLevelView(APIView):

    def post(self, request):
        product_stock = request.data

        serializer = serializers.ProductStockLevelSerializer(data=product_stock)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        
        product_stock = ProductStockLevel.objects.all()
        serializer = serializers.ProductStockLevelSerializer(data=product_stock, many=True)
        serializer.is_valid()

        return Response(serializer.data, status=200)

class ProductStockLevelDetailView(APIView):
    # def get_object(self, pk):
    #     try:
    #         return Product.objects.get(pk=pk)
    #     except Product.DoesNotExist:
    #         raise Http404

    # def get_queryset(self): #this method is called inside of get
    #     queryset = self.queryset.filter()
    #     return queryset

    def get_object(self, pk):
        # print(pk)
        try:
            return ProductStockLevel.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk, format=None):
        product_stock = self.get_object(pk)

        data = ProductStockLevel.objects.filter(id=product_stock.id).values()[0]
        serializer = serializers.ProductStockLevelSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def patch(self, request, *args, **kwargs):
        product_stock = self.get_object(pk=kwargs['pk'])
        serializer = serializers.ProductStockLevelSerializer(product_stock,
                                                            data=request.data, 
                                                            partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(data="wrong parameters", code=400)

    def delete(self, request, pk, format=None):
        product_stock = self.get_object(pk)
        product_stock.delete()
        return Response(status=204)

        
    def put(self, request, pk, format=None):
        product_stock = self.get_object(pk)
        serializer = serializers.ProductStockLevelSerializer(product_supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)