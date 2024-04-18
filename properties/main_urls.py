# person_plugin/main_urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='listing'),
    path('<int:item_id>/', views.property_detail, name='item_detail'),
    path('<int:pk>/edit/', views.edit_property, name='edit_property'),
]
    # path('adding', views.add_properties, name='adding'),
    # Add more URLs as needed

