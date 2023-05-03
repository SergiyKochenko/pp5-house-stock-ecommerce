from django.test import TestCase
from django.urls import reverse


class HireViewTestCase(TestCase):
    def test_hire_view_returns_200_status_code(self):
        url = reverse('hire')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_hire_view_uses_correct_template(self):
        url = reverse('hire')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'hire/hire.html')
