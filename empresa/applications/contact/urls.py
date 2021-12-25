from django.urls import path

from . import views

app_name = "contact_app"

urlpatterns = [
    path('contact/', views.RegistroContactFormview.as_view(), name='contact'),
]
