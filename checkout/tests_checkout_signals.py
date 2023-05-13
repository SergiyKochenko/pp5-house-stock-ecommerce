from django.test import TestCase
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from checkout.models import Order


class TestSignals(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword", email="test@example.com"
        )

        self.default_country = CountryField().formfield().choices[0][0]

        self.order = Order.objects.create(
            user=self.user,
            full_name="Test Name",
            email="test@example.com",
            phone_number="123456789",
            street_address1="Test Address",
            city="Test City",
            postcode="12345",
            country=self.default_country,
        )
