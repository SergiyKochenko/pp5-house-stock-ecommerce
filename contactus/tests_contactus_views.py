from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from .models import ContactUs


class ContactUsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contactUs_POST(self):
        response = self.client.post(reverse('contact_us'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'topic': 'Test message',
            'body': 'This is a test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactUs.objects.count(), 1)
        contact = ContactUs.objects.first()
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'johndoe@example.com')
        self.assertEqual(contact.topic, 'Test message')
        self.assertEqual(contact.body, 'This is a test message')

    def test_contactUs_valid(self):
        response = self.client.post(reverse('contact_us'), {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'topic': 'Test message',
            'body': 'This is a test message'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ContactForm({
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'topic': 'Test message',
            'body': 'This is a test message'
        }).is_valid())


