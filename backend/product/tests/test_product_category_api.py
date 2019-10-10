from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product, ProductCategory
import json

from product.serializers import ProductCategorySerializer, ProductSerializer

# def sample_product_category(name='Test Product Category #1', description='Test Description #1'):
#     ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
#     return ProductCategory.objects.values()[0].get('id')

PRODUCT_CATEGORY_ADD_URL = reverse('product:product_category_add')
PRODUCT_CATEGORIES_LIST_URL = reverse('product:product_category_list')
# PRODUCT_CATEGORIES_DETAIL_URL = reverse('product:product_category_details', args=(sample_product_category(),))


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
        ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
        # ProductCategory.objects.create(name='Test Product Category #2', description='Test Description #2')

        res = self.client.get(PRODUCT_CATEGORIES_LIST_URL, format='json')
        # print(PRODUCT_CATEGORIES_LIST_URL)
        product_categories = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(data=product_categories, many=True)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertDictEqual(dict(res.data), dict(serializer.data))
    
    def test_create_product_category_successful(self):
        """Test creating a new product category"""
        payload = {
            'product_category':{
                'name': 'Test Tag',
                'description': 'Test description'
            }
        }
        
        res = self.client.post(PRODUCT_CATEGORY_ADD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_product_category_detail(self):
        """Test viewing a product category detail"""
        ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
        pk = ProductCategory.objects.values()[0].get('id')
        # print(reverse('product:product_category_details', args=(pk,)))
        PRODUCT_CATEGORIES_DETAIL_URL = reverse('product:product_category_details', args=(pk,))
        res = self.client.get(PRODUCT_CATEGORIES_DETAIL_URL)
        print(res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    # def test_create_tag_invalid(self):
    #     """Test creating a new product category with invalid payload"""
    #     payload = {'name': 123}
    #     res = self.client.post(PRODUCT_CATEGORY_ADD_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)