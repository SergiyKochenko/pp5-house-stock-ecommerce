from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import testimonialForm
from .models import clientTestimonial


class TestimonialFormTest(TestCase):
    def setUp(self):
        self.form_data = {
            "name": "Test User",
            "testimonial": "This is a test testimonial.",
        }

    def test_valid_form(self):
        form = testimonialForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_required_fields(self):
        form_data = {}
        form = testimonialForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_missing_name(self):
        form_data = self.form_data.copy()
        del form_data["name"]
        form = testimonialForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_form_with_image(self):
        image_file = SimpleUploadedFile(
            name="0900631B81E48245M.jpg",
            content=open("media/0900631B81E48245M.jpg", "rb").read(),
            content_type="image/jpeg",
        )
        form_data = self.form_data.copy()
        form_data["image"] = image_file
        form = testimonialForm(data=form_data, files={"image": image_file})
        self.assertTrue(form.is_valid())

    def test_save_form(self):
        form = testimonialForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        form.save()
        self.assertEqual(clientTestimonial.objects.count(), 1)
