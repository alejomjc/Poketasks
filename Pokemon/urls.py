from django.urls import path
from .views import PokemonListCreateView, PokemonSearchView

urlpatterns = [
    path('pokemon/', PokemonListCreateView.as_view(), name='pokemon-list-create'),
    path('pokemon/search/', PokemonSearchView.as_view(), name='pokemon-search'),
]
