# from django.test import TestCase
# from django.contrib.auth.models import User
# from django_countries.fields import CountryField
# from decimal import Decimal

# from checkout.models import Order
# from profiles.models import UserProfile
# from django.conf import settings


# class TestOrderTotalLogic(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username="testuser",
#             password="testpassword",
#             email="test@example.com"
#         )

#         self.user_profile = UserProfile.objects.create(
#             user=self.user,
#             default_phone_number="123456789",
#             default_street_address1="Test Address",
#             default_city="Test City",
#             default_postcode="12345",
#         )

#         self.default_country = CountryField().formfield().choices[0][0]

#         self.user_profile = UserProfile.objects.create(
#             user=self.user,
#             default_phone_number='123456789',
#             default_street_address1='Test Address',
#             default_town_or_city='Test City',
#             default_postcode='12345',
#             default_country=self.default_country,
# )

#     def test_order_total_logic(self):
#         settings.FREE_DELIVERY_THRESHOLD = 100
#         settings.STANDARD_DELIVERY_PERCENTAGE = 10

#         # Test when order_total is below the free delivery threshold
#         self.order.order_total = Decimal('50.00')
#         self.order.update_total()
#         self.assertEqual(self.order.delivery_cost, Decimal('5.00'))
#         self.assertEqual(self.order.grand_total, Decimal('55.00'))

#         # Test when order_total is above the free delivery threshold
#         self.order.order_total = Decimal('150.00')
#         self.order.update_total()
#         self.assertEqual(self.order.delivery_cost, Decimal('0.00'))
#         self.assertEqual(self.order.grand_total, Decimal('150.00'))
