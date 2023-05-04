from django.test import TestCase
from .models import Category, Product, Wishlist, ProductReview
from django.contrib.auth.models import User


class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='test category',
            friendly_name='Test Category',
        )

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'test category')

    def test_get_friendly_name_method(self):
        self.assertEqual(self.category.get_friendly_name(), 'Test Category')


class TestProductModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='test category',
            friendly_name='Test Category',
        )
        self.product = Product.objects.create(
            category=self.category,
            sku='12345',
            name='test product',
            description='test description',
            has_sizes=True,
            price=10.00,
            in_stock=True,
            rating=4.5,
            image_url='https://test.com/image.png',
        )

    def test_product_str_method(self):
        self.assertEqual(str(self.product), 'test product')


class TestWishlistModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword',
        )
        self.category = Category.objects.create(
            name='test category',
            friendly_name='Test Category',
        )
        self.product = Product.objects.create(
            category=self.category,
            sku='12345',
            name='test product',
            description='test description',
            has_sizes=True,
            price=10.00,
            in_stock=True,
            rating=4.5,
            image_url='https://test.com/image.png',
        )
        self.wishlist = Wishlist.objects.create(
            product=self.product,
            user=self.user,
        )

    def test_wishlist_str_method(self):
        self.assertEqual(str(self.wishlist), 'test product')


class TestProductReviewModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword',
        )
        self.category = Category.objects.create(
            name='test category',
            friendly_name='Test Category',
        )
        self.product = Product.objects.create(
            category=self.category,
            sku='12345',
            name='test product',
            description='test description',
            has_sizes=True,
            price=10.00,
            in_stock=True,
            rating=4.5,
            image_url='https://test.com/image.png',
        )
        self.product_review = ProductReview.objects.create(
            product=self.product,
            user=self.user,
            content='test review',
            stars=4,
        )
