from django.urls import path
from . import views

urlpatterns = [
    path("contact/", views.contact, name="contact"), # Page de contact
    path("thanks/", views.thanks, name="thanks"), # Page de remerciement
]

