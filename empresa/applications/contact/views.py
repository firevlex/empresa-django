from django.shortcuts import render, redirect

from django.urls import reverse

from django.views.generic.edit import (
    FormView
)

from django.urls import reverse_lazy

from .forms import ContactForm

# Create your views here.
class RegistroContactFormview(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    #success_url = reverse_lazy('contact_app:contact')
    #success_url = reverse('contact')+'?ok'
    success_url = "?ok"