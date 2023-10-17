from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class PokemonSearchView(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Pokemon.objects.filter(name__icontains=name)
        return Pokemon.objects.all()