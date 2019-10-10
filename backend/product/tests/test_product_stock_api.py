from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProductSupplier, Supplier, Product, ProductCategory, ProductStockLevel
import json

from product.serializers import ProductStockLevelSerializer

import pytz
from datetime import datetime

PRODUCT_STOCK_ADD_URL = reverse('product:product_stock_add')
PRODUCT_STOCK_LIST_URL = reverse('product:product_stock_list')


class PrivatProductSupplierApiTests(TestCase):
    """Test the authorized user API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'test123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_product_stock_levels(self):
        """Test retrieving product stock level"""
        ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
        test_key_prodcat = ProductCategory.objects.values()[0]

        Product.objects.create(product_category_id=test_key_prodcat.get('id'), name='Test Product Category #2', description='Test Description #1', unit_price=12, quantity=15)
        test_key_product = Product.objects.values()[0]

        ProductStockLevel.objects.create(product_id=test_key_product.get('id'), quantity_level = 14, product_restocking=datetime.now(pytz.utc))
        res = self.client.get(PRODUCT_STOCK_LIST_URL, format='json')

        product_stocks= ProductStockLevel.objects.all()
        serializer = ProductStockLevelSerializer(data=product_stocks, many=True)
        serializer.is_valid()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertDictEqual(dict(res.data), dict(serializer.data))
    
    def test_create_product_category_successful(self):
        """Test creating a new product stock level"""
        
        ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
        test_key_prodcat = ProductCategory.objects.values()[0]

        Product.objects.create(product_category_id=test_key_prodcat.get('id'), name='Test Product Category #2', description='Test Description #1', unit_price=12, quantity=15)
        test_key_product = Product.objects.values()[0]

        payload = {
            # 'supplier':{
                'product_id': test_key_product.get('id'),
                'product_restocking': datetime.now(pytz.utc),
                'quantity_level': 140,
            # }
        }
        
        res = self.client.post(PRODUCT_STOCK_ADD_URL, payload)
        
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


    def test_create_product_category_invalid(self):
        """Test creating a malformed product stock level request"""
        payload = {
            # 'supplier':{
                'name': 'Test Tag',
                'email': 'newemail@email.com',
                'address': 'Test address'
            # }
        }
        
        res = self.client.post(PRODUCT_STOCK_ADD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)