from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm
from .models import ContactUs
from django.contrib.messages import get_messages


class ContactUsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contactUs_POST(self):
        response = self.client.post(
            reverse("contact_us"),
            {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "topic": "Test message",
                "body": "This is a test message",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactUs.objects.count(), 1)
        contact = ContactUs.objects.first()
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "johndoe@example.com")
        self.assertEqual(contact.topic, "Test message")
        self.assertEqual(contact.body, "This is a test message")

    def test_contactUs_valid(self):
        response = self.client.post(
            reverse("contact_us"),
            {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "topic": "Test message",
                "body": "This is a test message",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            ContactForm(
                {
                    "name": "John Doe",
                    "email": "johndoe@example.com",
                    "topic": "Test message",
                    "body": "This is a test message",
                }
            ).is_valid()
        )

    def test_contactForm_valid(self):
        """
        Test for valid form data
        """
        form_data = {
            "name": "Test User",
            "email": "testuser@example.com",
            "topic": "Test Subject",
            "body": "Test Message",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_contactForm_invalid(self):
        """
        Test for invalid form data
        """
        form_data = {}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("topic", form.errors)
        self.assertIn("body", form.errors)

    def test_contactUs_else(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ContactForm)

        messages_before = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages_before), 0)

        self.assertTemplateUsed(response, "contactus/contact_us.html")

        # make a POST request without data
        response = self.client.post(reverse("contact_us"))

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ContactForm)

        messages_after = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages_after), 1)
        self.assertEqual(messages_after[0], "Message not sent. Please try again.")

        # Test the else block
        response = self.client.get(reverse("contact_us") + "?submitted=1")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ContactForm)

        # Make a POST request with invalid data
        response = self.client.post(
            reverse("contact_us"),
            {"name": "", "email": "invalid_email", "topic": "", "body": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context["form"], ContactForm)

        messages_after = [m.message for m in get_messages(response.wsgi_request)]
        self.assertEqual(len(messages_after), 1)
        self.assertEqual(messages_after[0], "Message not sent. Please try again.")
