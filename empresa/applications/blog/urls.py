from django.urls import path

from . import views

app_name = "blog_app"

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
]
