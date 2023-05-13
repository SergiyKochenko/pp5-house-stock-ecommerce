from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.messages.storage.fallback import FallbackStorage


class SubscribeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("newsletter")
        self.valid_data = {"email": "test@example.com"}

    def test_subscribe_post(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "We have received your email.")

    def test_subscribe_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "newsletter/newsletter.html")
