#crearemos un template tag en esta seccion por medio de una funcion que utilizaremos para listar en el template base
#para obtener en forma de lista cada registro de lista

#ojo los templatetags que creamos de manera manual deben ser creados dentro de
#la cierta aplicacion o sino dara errores, como por ejemplo este template tag fue creado
#dentro de la aplicacion de pages

#esto lo estamos utilizando en el template 'base.html'
from django import template #para registrarlo en la libreria de templates de django
from applications.pages.models import Page

register = template.Library()

#transformamos una funcion, en un tag simple y lo registramos en la libraria de templates de django
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages






