from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Packages, CustomPackage
from .forms import PackageForm, CustomPackageForm


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.packages_url = reverse('packages')
        self.add_package_url = reverse('add_package')
        self.update_package_url = reverse('update_package', args=['1'])
        self.delete_package_url = reverse('delete_package', args=['1'])
        self.package_request_url = reverse('request')
        self.custom_packages_url = reverse('custom')
        self.delete_package_request_url = reverse('delete_package_request', args=['1'])

        self.package = Packages.objects.create(
            package_name="Test Package",
            equipment="Test Equipment",
            duration="1 Hour",
            home_items_included=False,
            home_items_type="",
            image_url="",
            discount_voucher=10.0,
            price=100.0,
        )

        self.custom_package = CustomPackage.objects.create(
            name="Test User",
            email="test@example.com",
            package_requirements="Test requirements",
        )

        self.user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            email="admin@example.com",
        )

    def test_CurrentPackages_view(self):
        response = self.client.get(self.packages_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages.html')

    def test_AddPackage_view(self):
        self.client.login(username='admin', password='adminpassword')

        response = self.client.get(self.add_package_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages_form.html')

    def test_UpdatePackage_view(self):
        self.client.login(username='admin', password='adminpassword')

        response = self.client.get(self.update_package_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages_form.html')

    def test_DeletePackage_view(self):
        self.client.login(username='admin', password='adminpassword')

        response = self.client.get(self.delete_package_url)

        self.assertEqual(response.status_code, 200)

    def test_PackageRequest_view(self):
        response = self.client.get(self.package_request_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/package_request_form.html')

    def test_PackageRequestList_view(self):
        self.client.login(username='admin', password='adminpassword')

        response = self.client.get(self.custom_packages_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/custom_packages.html')

    def test_DeletePackageRequest_view(self):
        self.client.login(username='admin', password='adminpassword')

        response = self.client.get(self.delete_package_request_url)

        self.assertEqual(response.status_code, 302)


class UpdatePackageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email='testemail@example.com'
        )
        self.package = Packages.objects.create(
            package_name="Test Package",
            discount_voucher=10,
            price=100
        )


class PackageRequestTest(TestCase):

    def test_package_request_view_uses_correct_template(self):
        response = self.client.get(reverse('request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/package_request_form.html')

    def test_package_request_form_submission(self):
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'package_requirements': 'Test package requirements'
        }
        response = self.client.post(reverse('request'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/package_request_success.html')
