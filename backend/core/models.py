from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
import uuid


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Supplier(models.Model):
    """Supplier object"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class ProductCategory(models.Model):
    """Product category object"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='N/A')

    # class Meta:
    #     name 
    def __repr__(self):
        return self.name


class ProductStockLevel(models.Model):
    quantity_level = models.IntegerField(default=1)
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    product_restocking = models.DateTimeField()


class Product(models.Model):
    """Product object"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='N/A')
    unit_price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.id)



class ProductSupplier(models.Model):
    """Product suppliers object"""
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE
    )
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE
    )
    date_to_supply = models.DateTimeField()
    quantity_supply = models.IntegerField()
    price = models.IntegerField()



# class Product(models.Model):
#     """Product model"""
#     product_name = models.CharField(max_length=255)
#     product_description = models.CharField(max_length=255)
    