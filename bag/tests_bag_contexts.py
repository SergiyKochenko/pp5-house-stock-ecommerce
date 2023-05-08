from decimal import Decimal
from django.test import TestCase, RequestFactory
from django.conf import settings
from products.models import Product
from .contexts import bag_contents


class BagContextsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
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

    def test_bag_contents(self):
        request = self.factory.get('/bag/')
        request.session = {'bag': {str(self.product1.pk): 2, str(self.product2.pk): 1}}
        
        context = bag_contents(request)

        self.assertEqual(len(context['bag_items']), 2)
        self.assertEqual(context['total'], 40)
        self.assertEqual(context['product_count'], 3)
        
        delivery = context['total'] * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        self.assertEqual(context['delivery'], delivery)
        self.assertEqual(context['free_delivery_threshold'], settings.FREE_DELIVERY_THRESHOLD)
        
        grand_total = delivery + context['total']
        self.assertEqual(context['grand_total'], grand_total)

        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - context['total']
        self.assertEqual(context['free_delivery_delta'], free_delivery_delta)
