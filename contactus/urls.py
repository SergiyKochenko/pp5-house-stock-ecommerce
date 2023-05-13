from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactUs, name='contact_us'),
]
