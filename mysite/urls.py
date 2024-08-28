from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path("home/", include("home.urls")), #Inclut les URL de l'application 'Home'
    path("admin/", admin.site.urls),
    path('', lambda request: redirect('home/', permanent=True)),
    path("contact/", include("contact.urls")),
]

