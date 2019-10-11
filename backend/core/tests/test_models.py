from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

def sample_product_category(name="categorytest", description="new description"):
    """Create a sample product category"""
    # product_category = models.ProductCategory.objects.all()
    return models.ProductCategory.objects.create(name, description)

# def sample_product_stock():


class ModelTests(TestCase):
    """Test model"""

    def test_create_user_with_email(self):
        """"Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_new_supplier(self):
        """Test creating a new supplier"""
        supplier = models.Supplier.objects.create(
            email="new_supplier@supplier.test",
            name="Supplier test",
            address="Address new #1"
        )

        self.assertEqual(str(supplier), supplier.email)

    def test_create_new_product_category(self):
        """Test creating a new product category"""
        product_category = models.ProductCategory.objects.create(
            name="new product",
            description="test description"
        )

        self.assertEqual(repr(product_category), product_category.name)

    def test_create_new_product(self):
        """Test creating a new product"""
        

        # print('awww' + sample_product_category(name="newname", description="descript"))
        product_categoryfk = models.ProductCategory.objects.create(
            name="testproductcategory",
            description="wwwwww"
        )

        product = models.Product.objects.create(
            product_category=product_categoryfk,
            name="new product",
            description="test description",
            unit_price=5,
            quantity=1
        )

        self.assertEqual(str(product), str(product.id))
    # def test_tag_str(self):
    #     """Test the tag string representation"""
    #     tag = models.Tag.objects.create(
    #         user=sample_user(),
    #         name='Meatlover'
    #     )

    #     self.assertEqual(str(tag), tag.name)
