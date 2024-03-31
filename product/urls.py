from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("create-requirement/", views.create_requirement),
]