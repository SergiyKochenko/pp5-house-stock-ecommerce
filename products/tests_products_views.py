from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.contrib.auth.models import User


class TestAllProductsView(TestCase):
    def setUp(self):
        self.url = reverse("products")
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(
            name="Test Product",
            price=10,
            category=self.category,
        )

    def test_all_products_view_with_search_query(self):
        response = self.client.get(self.url, {"q": "test"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertQuerysetEqual(
            response.context["products"], ["<Product: Test Product>"]
        )

    def test_all_products_view_with_sorting(self):
        response = self.client.get(self.url, {"sort": "name"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")
        self.assertQuerysetEqual(
            response.context["products"], ["<Product: Test Product>"]
        )
