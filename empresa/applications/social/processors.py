#Los processors nos sirven para que los valores de los diccionarios que
#creamos aca se vean en cualquier templates , usando sus key.

#para usarlo se va a settings y en base en TEMPLATES:
"""
           'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                ACA SE ANADE EL NUEVO PROCESSOR
            ],
"""

from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx

