from django.db import models


class clientTestimonial(models.Model):
    """
    Model class for the testimonials app
    """
    name = models.CharField(max_length=256)
    testimonial = models.TextField(blank=True, null=True)
    photo_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        "Testimonial Image", default='placeholder')

    def __str__(self):
        return self.name