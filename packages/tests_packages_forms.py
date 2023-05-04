from django.test import TestCase
from .forms import PackageForm, CustomPackageForm


class TestPackageForm(TestCase):

    def test_package_form_valid_data(self):
        form = PackageForm(data={
            'package_name': 'Test Package',
            'equipment': 'Equipment for test package',
            'duration': '3 hours',
            'home_items_included': True,
            'home_items_type': 'Type of home items for test package',
            'discount_voucher': 10.0,
            'price': 50.0
        })

        self.assertTrue(form.is_valid())

    def test_package_form_invalid_data(self):
        form = PackageForm(data={
            'package_name': '',
            'discount_voucher': 'invalid'
        })

        self.assertFalse(form.is_valid())


class TestCustomPackageForm(TestCase):

    def test_custom_package_form_valid_data(self):
        form = CustomPackageForm(data={
            'name': 'Test User',
            'email': 'testuser@example.com',
            'package_requirements': 'Requirements for custom package'
        })

        self.assertTrue(form.is_valid())

    def test_custom_package_form_invalid_data(self):
        form = CustomPackageForm(data={
            'name': '',
            'email': 'invalidemail',
            'package_requirements': ''
        })

        self.assertFalse(form.is_valid())
