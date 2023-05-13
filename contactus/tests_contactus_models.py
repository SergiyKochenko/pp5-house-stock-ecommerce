from django.test import TestCase
from .models import ContactUs


class ContactUsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ContactUs.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            topic="Test topic",
            body="Test body",
        )

    def test_name_label(self):
        contact_us = ContactUs.objects.get(id=1)
        field_label = contact_us._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_email_label(self):
        contact_us = ContactUs.objects.get(id=1)
        field_label = contact_us._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "email")

    def test_topic_label(self):
        contact_us = ContactUs.objects.get(id=1)
        field_label = contact_us._meta.get_field("topic").verbose_name
        self.assertEqual(field_label, "topic")

    def test_body_label(self):
        contact_us = ContactUs.objects.get(id=1)
        field_label = contact_us._meta.get_field("body").verbose_name
        self.assertEqual(field_label, "body")

    def test_created_on_label(self):
        contact_us = ContactUs.objects.get(id=1)
        field_label = contact_us._meta.get_field("created_on").verbose_name
        self.assertEqual(field_label, "created on")

    def test_name_max_length(self):
        contact_us = ContactUs.objects.get(id=1)
        max_length = contact_us._meta.get_field("name").max_length
        self.assertEqual(max_length, 254)

    def test_topic_max_length(self):
        contact_us = ContactUs.objects.get(id=1)
        max_length = contact_us._meta.get_field("topic").max_length
        self.assertEqual(max_length, 254)

    def test_object_name_is_topic_from_name(self):
        contact_us = ContactUs.objects.get(id=1)
        expected_object_name = f"Message {contact_us.topic} from {contact_us.name}"
        self.assertEqual(str(contact_us), expected_object_name)
