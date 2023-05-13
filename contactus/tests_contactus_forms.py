from django.test import TestCase
from .forms import ContactForm


class ContactFormTestCase(TestCase):
    def test_form_labels(self):
        form = ContactForm()
        self.assertEqual(form.fields["name"].label, False)
        self.assertEqual(form.fields["email"].label, False)
        self.assertEqual(form.fields["topic"].label, False)
        self.assertEqual(form.fields["body"].label, False)

    def test_form_with_valid_data(self):
        form_data = {
            "name": "Test User",
            "email": "test@example.com",
            "topic": "Test Topic",
            "body": "Test message body.",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form_data = {
            "name": "",
            "email": "invalid-email",
            "topic": "",
            "body": "",
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("topic", form.errors)
        self.assertIn("body", form.errors)
