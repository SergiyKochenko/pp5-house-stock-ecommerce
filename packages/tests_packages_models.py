from django.test import TestCase
from .models import Packages, CustomPackage


class TestModels(TestCase):
    def setUp(self):
        self.package = Packages.objects.create(
            package_name="Test Package",
            equipment="Test Equipment",
            duration="Test Duration",
            home_items_included=True,
            home_items_type="Test Home Items Type",
            image_url="https://test_image_url.com",
            discount_voucher=5.0,
            price=100.0,
        )
        self.custom_package = CustomPackage.objects.create(
            name="Test User",
            email="test@example.com",
            package_requirements="Test Requirements",
        )

    def test_package_str(self):
        self.assertEqual(str(self.package), "Test Package")

    def test_custom_package_str(self):
        self.assertEqual(str(self.custom_package), "Test User")
