from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    def test_product_form_image_field_label(self):
        form = ProductForm()
        self.assertTrue(form.fields["image"].label == "Image")

    def test_product_form_image_field_required(self):
        form = ProductForm()
        self.assertFalse(form.fields["image"].required)

    def test_product_form_image_field_widget(self):
        form = ProductForm()
        self.assertTrue(
            form.fields["image"].widget.__class__.__name__ == "CustomClearableFileInput"
        )

    def test_product_form_category_field_choices(self):
        form = ProductForm()
        categories = form.fields["category"].choices
        self.assertEqual(len(categories), 0)

    def test_product_form_field_classes(self):
        form = ProductForm()
        self.assertEqual(
            form.fields["sku"].widget.attrs["class"], "border-black rounded-0"
        )
        self.assertEqual(
            form.fields["name"].widget.attrs["class"], "border-black rounded-0"
        )
        self.assertEqual(
            form.fields["description"].widget.attrs["class"], "border-black rounded-0"
        )
        self.assertEqual(
            form.fields["has_sizes"].widget.attrs["class"], "border-black rounded-0"
        )
        self.assertEqual(
            form.fields["price"].widget.attrs["class"], "border-black rounded-0"
        )
        self.assertEqual(
            form.fields["in_stock"].widget.attrs["class"], "border-black rounded-0"
        )
