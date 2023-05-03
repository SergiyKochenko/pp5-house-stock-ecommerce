from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


def contactUs(request):
    """
    a view to display the contactform
    and handle form submission
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/contactus?submitted=True')
        else:
            messages.warning(request, 'Message not sent. Please try again.')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            form = ContactForm()

    template = 'contactus/contact_us.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
