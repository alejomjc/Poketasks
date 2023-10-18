from requests import Response
from rest_framework import generics, status
from .models import Pokemon, Ability
import logging
from .serializers import PokemonSerializer
from rest_framework import generics
from .tasks import get_random_pokemon
from rest_framework.exceptions import AuthenticationFailed

get_random_pokemon.apply_async(countdown=0)
logger = logging.getLogger(__name__)


class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        try:
            ability_data = request.data.pop('abilities', [])
            pokemon_name = request.data.get('name')
            existing_pokemon = Pokemon.objects.filter(name=pokemon_name).exists()

            for data in ability_data:
                ability_info = data.get('ability', {})
                ability, created = Ability.objects.get_or_create(name=ability_info.get('name'))

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            pokemon = serializer.instance

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            raise AuthenticationFailed(detail=str(e))


class PokemonSearchView(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Pokemon.objects.filter(name__icontains=name)
        return Pokemon.objects.all()
