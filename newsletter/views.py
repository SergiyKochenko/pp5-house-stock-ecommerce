from django.shortcuts import render
from django.contrib import messages


def subscribe(request):
    """
    A View to handle email when user submit
    form
    """
    if request.method == "POST":
        messages.success(request, "We have received your email.")

    return render(request, "newsletter/newsletter.html")
