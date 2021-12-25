from django.urls import path

from . import views

app_name = "page_app"

urlpatterns = [
    path('sample/<pk>/', views.Detalle_Pagina.as_view(), name='sample'),
]
