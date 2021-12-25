from django.urls import path

from . import views

app_name = "service_app"

urlpatterns = [
    path('services/', views.servicesListView.as_view(), name='services'),
]
