from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    def test_review_form_stars_field_label(self):
        form = ReviewForm()
        self.assertTrue(form.fields["stars"].label == "Stars")

    def test_review_form_content_field_label(self):
        form = ReviewForm()
        self.assertTrue(form.fields["content"].label == "Content")

    def test_review_form_stars_field_widget(self):
        form = ReviewForm()
        self.assertTrue(form.fields["stars"].widget.__class__.__name__ == "NumberInput")

    def test_review_form_content_field_widget(self):
        form = ReviewForm()
        self.assertTrue(form.fields["content"].widget.__class__.__name__ == "Textarea")

    def test_review_form_fields(self):
        form = ReviewForm()
        self.assertEqual(len(form.fields), 2)
        self.assertTrue("stars" in form.fields)
        self.assertTrue("content" in form.fields)
