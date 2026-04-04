from django.urls import path
from . import views

urlpatterns = [
    path('article/', views.liste_article, name = 'liste_article')
]
