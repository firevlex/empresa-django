from django.shortcuts import render

from .models import Page

from django.views.generic import DetailView


# Create your views here.
class Detalle_Pagina(DetailView):
    model = Page
    template_name = 'page/sample.html'