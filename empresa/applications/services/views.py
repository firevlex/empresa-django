from django.shortcuts import render
from django.views.generic import ListView

from .models import Service
# Create your views here.
class servicesListView(ListView):
    model = Service
    template_name = 'services/services.html'
    ordering = 'created'
    context_object_name='services'

