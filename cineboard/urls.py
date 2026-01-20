from django.urls import path
from .views import (
    FilmListView, FilmDetailView,
    FilmCreateView, FilmUpdateView, FilmDeleteView,
    RegisterView
)
from .views import toggle_like



urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),
    path('film/<int:pk>/', FilmDetailView.as_view(), name='film_detail'),
    path('film/add/', FilmCreateView.as_view(), name='film_add'),
    path('film/<int:pk>/edit/', FilmUpdateView.as_view(), name='film_edit'),
    path('film/<int:pk>/delete/', FilmDeleteView.as_view(), name='film_delete'),
    path('register/', RegisterView.as_view(), name='register'),
    path('film/<int:pk>/like/', toggle_like, name='film_like'),

]






