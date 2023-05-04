from django.test import TestCase
from .models import clientTestimonial

class TestClientTestimonialModel(TestCase):

    def setUp(self):
        self.testimonial = clientTestimonial.objects.create(
            name="Test User",
            testimonial="This is a test testimonial.",
            photo_url="https://www.example.com/test.jpg",
        )

    def test_clientTestimonial_model(self):
        self.assertEqual(self.testimonial.name, "Test User")
        self.assertEqual(self.testimonial.testimonial, "This is a test testimonial.")
        self.assertEqual(self.testimonial.photo_url, "https://www.example.com/test.jpg")
        self.assertEqual(str(self.testimonial), "Test User")
