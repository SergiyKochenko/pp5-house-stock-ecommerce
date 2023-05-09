# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from unittest.mock import patch
# from .models import Order, OrderLineItem
# from .forms import OrderForm
# from products.models import Product

# from unittest.mock import patch
# from django.urls import reverse

# # Test the views
# class CheckoutViewTests(TestCase):
#     def setUp(self):
#         # Create test user
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     @patch('checkout.views.stripe')
#     def test_checkout_view_uses_correct_template(self, mock_stripe):
#         mock_stripe.Charge.create.return_value = {'id': 'fake_charge_id'}
#         self.client.login(username='testuser', password='testpassword')
#         response = self.client.get(reverse('checkout'))
#         self.assertTemplateUsed(response, 'checkout/checkout.html')

# # Test the forms
# class OrderFormTests(TestCase):
#     def test_order_form_valid_data(self):
#         form = OrderForm(data={
#             'full_name': 'John Doe',
#             'email': 'john.doe@example.com',
#             'phone_number': '1234567890',
#             'street_address1': '123 Street',
#             'town_or_city': 'Test City',
#             'postcode': '12345',
#             'country': 'US',
#             'county': 'Test County',
#         })
#         self.assertTrue(form.is_valid())

#     def test_order_form_invalid_data(self):
#         form = OrderForm(data={})
#         self.assertFalse(form.is_valid())

# # Test the models
# class OrderModelTests(TestCase):
#     def test_order_creation(self):
#         order = Order.objects.create(
#             full_name='John Doe',
#             email='john.doe@example.com',
#             phone_number='1234567890',
#             street_address1='123 Street',
#             town_or_city='Test City',
#             postcode='12345',
#             country='US',
#             county='Test County',
#         )
#         self.assertEqual(str(order), order.order_number)

# class OrderLineItemModelTests(TestCase):
#     def setUp(self):
#         self.order = Order.objects.create(
#             full_name='John Doe',
#             email='john.doe@example.com',
#             phone_number='1234567890',
#             street_address1='123 Street',
#             town_or_city='Test City',
#             postcode='12345',
#             country='US',
#             county='Test County',
#         )
#         self.product = Product.objects.create(
#             name='Test Product',
#             description='Test Description',
#             price=9.99,
#         )

#     def test_order_line_item_creation(self):
#         order_line_item = OrderLineItem.objects.create(
#             order=self.order,
#             product=self.product,
#             quantity=1,
#         )
#         self.assertEqual(str(order_line_item), f'SKU {self.product.sku} on order {self.order.order_number}')



# @patch('checkout.views.stripe')
# def test_checkout_view_uses_correct_template(self, mock_stripe):
#     # Mock the Stripe API call
#     mock_stripe.Charge.create.return_value = {'id': 'fake_charge_id'}

#     # Log in the test user
#     self.client.login(username='testuser', password='testpassword')

#     # Make a request to the checkout view
#     response = self.client.get(reverse('checkout'))

#     # Assert that the correct template is used
#     self.assertTemplateUsed(response, 'checkout/checkout.html')

