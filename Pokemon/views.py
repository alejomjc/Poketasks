from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, extend_schema_view
import json
from .models import Pokemon, Ability
from .serializers import PokemonSerializer
from rest_framework import generics


@extend_schema_view(
    list=extend_schema(description='Permite agregar la descripcion')
)
class PokemonListCreateView(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            ability_data = request.data['abilities']
            pokemon_name = request.data['name']

            if not Pokemon.objects.filter(name=pokemon_name).exists():
                pokemon = Pokemon(name=pokemon_name, api_creation=True)
                pokemon.save()

                for data in ability_data:
                    ability_info = data['ability']
                    ability, created = Ability.objects.get_or_create(name=ability_info['name'])
                    pokemon.ability.add(ability)
                pokemon.save()

                return Response({'message': 'True'}, status=status.HTTP_200_OK)
            else:
                log_data = {
                    "name": pokemon_name,
                    "abilities": [ability_info['ability']['name'] for ability_info in ability_data]
                }
                save_to_json(log_data)
                return Response({'message': 'Pokemon have already exists'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            raise error


class PokemonSearchView(generics.ListAPIView):
    serializer_class = PokemonSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name is not None:
            return Pokemon.objects.filter(name__icontains=name)
        return Pokemon.objects.none()


def save_to_json(data):
    with open('pokemon_logs.log', 'a') as log_file:
        log_file.write(json.dumps(data) + '\n')
