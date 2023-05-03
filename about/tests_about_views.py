from django.test import TestCase
from django.urls import reverse


class AboutViewTestCase(TestCase):
    def test_about_view_returns_200_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_about_view_uses_correct_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about/about.html')
