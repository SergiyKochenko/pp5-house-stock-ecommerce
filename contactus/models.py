from django.db import models


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'

    name = models.CharField(max_length=254)
    email = models.EmailField()
    topic = models.CharField(max_length=254)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.topic} from {self.name}"
