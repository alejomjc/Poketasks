from rest_framework import serializers
from .models import Pokemon, Ability


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = ['id', 'name']


class PokemonSerializer(serializers.ModelSerializer):
    ability = AbilitySerializer(many=True)
    api_creation = serializers.BooleanField(default=True)

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'ability', 'api_creation']
