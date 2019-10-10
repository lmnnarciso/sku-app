from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Supplier
import json

from supplier.serializers import SupplierSerializer

SUPPLIER_ADD_URL = reverse('supplier:add')
SUPPLIERS_LIST_URL = reverse('supplier:list')


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
        Supplier.objects.create(name='Test Product Category #1', email='test@test.com', address='Test Address #1')
        # ProductCategory.objects.create(name='Test Product Category #2', description='Test Description #2')

        res = self.client.get(SUPPLIERS_LIST_URL, format='json')
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(data=suppliers, many=True)
        serializer.is_valid()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # self.assertDictEqual(dict(res.data), dict(serializer.data))
    
    def test_create_product_category_successful(self):
        """Test creating a new product category"""
        payload = {
            # 'supplier':{
                'name': 'Test Tag',
                'email': 'newemail@email.com',
                'address': 'Test address'
            # }
        }
        
        res = self.client.post(SUPPLIER_ADD_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)