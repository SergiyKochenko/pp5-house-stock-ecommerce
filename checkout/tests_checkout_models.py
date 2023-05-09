from django.test import TestCase
from decimal import Decimal
from django_countries.fields import Country
from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem
from django.contrib.auth.models import User


class TestOrderLineItemModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.order = Order.objects.create(
            user_profile=self.profile,
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country=Country('US'),
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 1',
            county='Test County',
            delivery_cost=Decimal('5.00'),
            order_total=Decimal('10.00'),
            grand_total=Decimal('15.00'),
            original_bag='{}',
            stripe_pid='test_stripe_pid'
        )
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=Decimal('10.00'),
            sku='TESTSKU',
        )
        self.order_line_item = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            product_size='M',
            quantity=1,
            lineitem_total=Decimal('10.00'),
        )

    def test_order_line_item_model_str(self):
        self.assertEqual(str(self.order_line_item), f'SKU {self.product.sku} on order {self.order.order_number}')


class TestOrderLineItemModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile, _ = UserProfile.objects.get_or_create(user=self.user)
        self.order = Order.objects.create(
            user_profile=self.profile,
            full_name='Test User',
            email='test@example.com',
            phone_number='123456789',
            country=Country('US'),
            town_or_city='Test City',
            street_address1='123 Test Street',
            street_address2='Apt 1',
            county='Test County',
            delivery_cost=Decimal('5.00'),
            order_total=Decimal('10.00'),
            grand_total=Decimal('15.00'),
            original_bag='{}',
            stripe_pid='test_stripe_pid'
        )

    def test_order_model_str(self):
        self.assertEqual(str(self.order), self.order.order_number)
