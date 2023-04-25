from django.db import models
from cloudinary.models import CloudinaryField


class Packages(models.Model):
    """
    Model class for the packages app
    """

    class Meta:
        verbose_name_plural = 'Packages'

    package_name = models.CharField(max_length=256)
    equipment = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    home_items_included = models.BooleanField(
        default=False, null=True, blank=True)
    home_items_type = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, blank=True, null=True)
    image = CloudinaryField(
        "Package Image", default='https://res.cloudinary.com/dvbhrs1gf/image/upload/v1682439593/WebP_File_Format_qjtvp8.png')
    discount_voucher = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2, blank=True,  null=True)

    def __str__(self):
        return self.package_name


class CustomPackage(models.Model):
    """ Model for Contact """

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    package_requirements = models.TextField(max_length=600, default='')

    def __str__(self):
        return self.name
