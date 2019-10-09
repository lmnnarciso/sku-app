from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Product, ProductCategory

from product.serializers import ProductCategorySerializer, ProductSerializer

PRODUCT_CATEGORY_ADD_URL = reverse('product:product_category_add')
PRODUCT_CATEGORIES_LIST_URL = reverse('product:product_category_list')
PRODUCT_CATEGORIES_DETAIL_URL = reverse('product:product_category_list')


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
        ProductCategory.objects.create(name='Test Product Category #2', description='Test Description #2')

        res = self.client.get(PRODUCT_CATEGORIES_LIST_URL)

        product_categories = ProductCategory.objects.all().order_by('-name')
        serializer = ProductCategorySerializer(product_categories, many=True)
        print( serializer.data[0])
        print('========================')
        print( res.data[0])

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(dict(res.data), dict(serializer.data))
