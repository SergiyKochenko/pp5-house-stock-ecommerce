from django.test import TestCase
from contactus.forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_form_valid_data(self):
        form = ContactForm({
            'name': 'John Smith',
            'email': 'john.smith@example.com',
            'topic': 'Test Topic',
            'body': 'Test message body',
        })

        self.assertTrue(form.is_valid())

    def test_contact_form_missing_data(self):
        form = ContactForm({
            'name': '',
            'email': '',
            'topic': '',
            'body': '',
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)