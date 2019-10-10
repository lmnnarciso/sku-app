from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ProductSupplier, Supplier, Product, ProductCategory
import json

from supplier.serializers import ProductSupplierSerializer

import pytz
from datetime import datetime

PRODUCT_SUPPLIER_ADD_URL = reverse('supplier:product_supplier_add')
PRODUCT_SUPPLIERS_LIST_URL = reverse('supplier:product_supplier_list')


class PrivatSuppliersApiTests(TestCase):
    """Test the authorized user API"""

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
        test_key_prodcat = ProductCategory.objects.values()[0]

        Supplier.objects.create(name='Test Supplier #1', email='test@test.com', address='Test Address #1')
        test_key_supplier = Supplier.objects.values()[0]

        Product.objects.create(product_category_id=test_key_prodcat.get('id'), name='Test Product Category #2', description='Test Description #1', unit_price=12, quantity=15)
        test_key_product = Product.objects.values()[0]

        ProductSupplier.objects.create(product_id=test_key_product.get('id'), supplier_id=test_key_supplier.get('id'), date_to_supply=datetime.now(pytz.utc), quantity_supply=140, price = 1230)
        res = self.client.get(PRODUCT_SUPPLIERS_LIST_URL, format='json')

        product_suppliers = ProductSupplier.objects.all()
        serializer = ProductSupplierSerializer(data=product_suppliers, many=True)
        serializer.is_valid()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertDictEqual(dict(res.data), dict(serializer.data))
    
    def test_create_product_category_successful(self):
        """Test creating a new product category"""
        
        ProductCategory.objects.create(name='Test Product Category #1', description='Test Description #1')
        test_key_prodcat = ProductCategory.objects.values()[0]

        Supplier.objects.create(name='Test Supplier #1', email='test@test.com', address='Test Address #1')
        test_key_supplier = Supplier.objects.values()[0]

        Product.objects.create(product_category_id=test_key_prodcat.get('id'), name='Test Product Category #2', description='Test Description #1', unit_price=12, quantity=15)
        test_key_product = Product.objects.values()[0]
        
        payload = {
            # 'supplier':{
                'product_id': test_key_product.get('id'),
                'supplier_id': test_key_supplier.get('id'),
                'date_to_supply': datetime.now(pytz.utc),
                'quantity_supply': 140,
                'price': 1400,
            # }
        }
        
        res = self.client.post(PRODUCT_SUPPLIER_ADD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_product_category_invalid(self):
        """Test creating a new product category"""
        payload = {
            # 'supplier':{
                'name': 'Test Tag',
                'email': 'newemail@email.com',
                'address': 'Test address'
            # }
        }
        
        res = self.client.post(PRODUCT_SUPPLIER_ADD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)