from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(
        default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    """
    Model for users to save their favoutite
    products to a wishlist
    """
    product = models.ForeignKey(
        Product, related_name='wishlist', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class ProductReview(models.Model):
    """
    Model for product reviews
    """
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
