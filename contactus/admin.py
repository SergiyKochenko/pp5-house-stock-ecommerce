from django.contrib import admin
from .models import ContactUs


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'topic', 'created_on')
    search_fields = ('name', 'email', 'topic', 'body')
    list_filter = ('name', 'email')
