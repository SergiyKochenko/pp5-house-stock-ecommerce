from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class BagViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.view_bag_url = reverse('view_bag')
        self.test_product = Product.objects.create(
            name='Test Product',
            description='Test Product Description',
            price=9.99,
        )
        self.add_to_bag_url = reverse('add_to_bag', args=[self.test_product.pk])
        self.adjust_bag_url = reverse('adjust_bag', args=[self.test_product.pk])
        self.remove_from_bag_url = reverse('remove_from_bag', args=[self.test_product.pk])

    def test_view_bag_view_uses_correct_template(self):
        response = self.client.get(self.view_bag_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_view(self):
        response = self.client.post(self.add_to_bag_url, {'quantity': 1, 'redirect_url': '/'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['bag'][str(self.test_product.pk)], 1)

    def test_adjust_bag_view(self):
        self.client.session['bag'] = {str(self.test_product.pk): 1}
        self.client.session.save()

        response = self.client.post(self.adjust_bag_url, {'quantity': 2})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['bag'][str(self.test_product.pk)], 2)

    # def test_remove_from_bag_view(self):
    #     self.client.session['bag'] = {str(self.test_product.pk): 1}
    #     self.client.session.save()

    #     response = self.client.post(self.remove_from_bag_url)

    #     if response.status_code != 200:
    #         print(response.content)  # Add this line to print the error message in the response

    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotIn(str(self.test_product.pk), self.client.session['bag'])

