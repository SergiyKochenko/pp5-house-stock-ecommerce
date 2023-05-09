from django.test import TestCase
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from checkout.models import Order


# from checkout.signals import save_order_handler, delete_order_handler




# Add any other necessary imports for your models and signals


class TestSignals(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="test@example.com"
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

    # def test_update_on_save_signal(self):
    #     # Create a new Order object
    #     new_order = Order.objects.create(
    #         user=self.user,
    #         full_name="New Test Name",
    #         email="newtest@example.com",
    #         phone_number="987654321",
    #         street_address1="New Test Address",
    #         city="New Test City",
    #         postcode="67890",
    #         country=self.default_country,
    #     )

    #     # Connect the signal
    #     save_order_handler.connect(self.order)

    #     # Save the Order object
    #     new_order.save()

    #     # Test if the signal was triggered and updated the order object correctly
    #     updated_order = Order.objects.get(pk=new_order.pk)
    #     self.assertEqual(updated_order.full_name, "New Test Name")

    # def test_update_on_delete_signal(self):
    #     # Create a new Order object
    #     new_order = Order.objects.create(
    #         user=self.user,
    #         full_name="New Test Name",
    #         email="newtest@example.com",
    #         phone_number="987654321",
    #         street_address1="New Test Address",
    #         city="New Test City",
    #         postcode="67890",
    #         country=self.default_country,
    #     )

    #     # Connect the signal
    #     delete_order_handler.connect(self.order)

    #     # Delete the Order object
    #     new_order.delete()

    #     # Test if the signal was triggered and updated the order object correctly
    #     self.assertRaises(Order.DoesNotExist, Order.objects.get, pk=new_order.pk)
