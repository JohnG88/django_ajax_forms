from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_add_view, name='photo_add_view'),
]