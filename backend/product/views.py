from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse

from core.models import ProductCategory, Product
from product import serializers


class ProductCategoryListView(APIView):
    serializer_class = serializers.ProductCategorySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        product_category = request.data.get('product_category')
        # print(product_category)
        serializer = serializers.ProductCategorySerializer(data=product_category)
        if serializer.is_valid(raise_exception=True):
            product_category_saved = serializer.save()
        return Response({"success": "Product Category '{}' created successfully".format(product_category_saved.name)})

    def get(self, request):
        product_category = ProductCategory.objects.all()
        serializer = serializers.ProductCategorySerializer(data=product_category, many=True)
        serializer.is_valid()
        print(Response(serializer.data))
        return Response(serializer.data)

class ProductCategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = serializers.ProductCategorySerializer(product_category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product_category = self.get_object(pk)
        serializer = serializers.ProductCategorySerializer(product_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product_category = self.get_object(pk)
        product_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductView(APIView):
    """for Product API requests"""
    def post(self, request):
        product = request.data.get('product')
        print(product)
        serializer = serializers.ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_category_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_category_saved.name)})

    def get(self, request):
        product = Product.objects.all()
        serializer = serializers.ProductSerializer(data=product, many=True)
        serializer.is_valid()
        return JsonResponse(serializer.data, safe=False)

class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = serializers.ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)