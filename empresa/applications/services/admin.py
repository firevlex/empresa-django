from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') #para que se vean estos campos, y sean ded lectura ya que django no los muestra por defecto.

admin.site.register(Service, ServiceAdmin)



