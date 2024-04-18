# person_plugin/main_urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_properties, name='adding'),
    # Add more URLs as needed
]
