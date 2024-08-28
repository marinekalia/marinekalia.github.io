from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),  #Page d'acceuil   
    path("score/",views.score, name="score"),  #Page de score 
    path("about/",views.about, name = "about"), #Page About  
]
