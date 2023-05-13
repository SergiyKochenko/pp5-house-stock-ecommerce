from django.test import TestCase
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from .forms import OrderForm
from .models import Order


class TestOrderForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_order_form_valid(self):
        form_data = {
            "full_name": "Test User",
            "email": "testuser@example.com",
            "phone_number": "1234567890",
            "country": "US",
            "postcode": "12345",
            "town_or_city": "Test City",
            "street_address1": "Test Street 1",
            "street_address2": "Test Street 2",
            "county": "Test County",
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_order_form_invalid(self):
        form_data = {
            "full_name": "",
            "email": "testuser@example.com",
            "phone_number": "1234567890",
            "country": "US",
            "postcode": "12345",
            "town_or_city": "Test City",
            "street_address1": "Test Street 1",
            "street_address2": "Test Street 2",
            "county": "Test County",
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["full_name"], ["This field is required."])
