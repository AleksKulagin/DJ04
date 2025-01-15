from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_film, name='create_film'),
    path('', views.film_list, name='film_list'),
]