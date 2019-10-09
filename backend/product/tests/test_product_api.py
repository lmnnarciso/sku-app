from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product, ProductCategory

from product.serializers import ProductCategorySerializer, ProductSerializer

PRODUCT_ADD_URL = reverse('product:product')
PRODUCTS_LIST_URL = reverse('product:product_add')
# PRODUCT_DETAIL_URL = reverse('product:product_detail')


class PrivateProductCategoriesApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'test123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_product_categories(self):
        """Test retrieving tags"""
        # test_key = ProductCategory.objects. 
        Product.objects.create(product_category_id=1, name='Test Product Category #1', description='Test Description #1', unit_price=12, quantity=15)
        # ProductCategory.objects.create(name='Test Product Category #2', description='Test Description #2')

        res = self.client.get(PRODUCTS_LIST_URL)

        products = Product.objects.all().order_by('-name')
        serializer = ProductSerializer(products, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertDictEqual(dict(res.data), dict(serializer.data))
    
    # def test_create_product_category_successful(self):
    #     """Test creating a new product category"""
    #     payload = {
    #         'product_category':{
    #             'name': 'Test Tag',
    #             'description': 'Test description'
    #         }
    #     }
        
    #     res = self.client.post(PRODUCT_CATEGORY_ADD_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_create_tag_invalid(self):
    #     """Test creating a new product category with invalid payload"""
    #     payload = {'name': 123}
    #     res = self.client.post(PRODUCT_CATEGORY_ADD_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)