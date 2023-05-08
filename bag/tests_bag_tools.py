from django.test import TestCase
from products.models import Product
from bag.templatetags.bag_tools import calc_subtotal


class BagToolsTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            name="Test Product 1",
            description="Test product 1 description",
            price=10.00,
        )
        self.product2 = Product.objects.create(
            name="Test Product 2",
            description="Test product 2 description",
            price=20.00,
        )

    def test_calc_subtotal(self):
        subtotal1 = calc_subtotal(self.product1.price, 2)
        self.assertEqual(subtotal1, 20.00)

        subtotal2 = calc_subtotal(self.product2.price, 3)
        self.assertEqual(subtotal2, 60.00)
