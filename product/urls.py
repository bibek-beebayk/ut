from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("products/", views.products),
    path("about/", views.about_us),
    path("contact/", views.contact_us)
]