from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from unittest.mock import patch
from .tasks import get_random_pokemon
import requests
import json

from .models import Ability, Pokemon


class GetRandomPokemonTestCase(TestCase):

    @patch('Pokemon.tasks.get_random_pokemon')
    def test_my_celery_task(self, mock_task):
        mock_task.apply_async.return_value = None
        result = get_random_pokemon()
        self.assertEqual(result.status_code, status.HTTP_200_OK)


class PokemonAPITestCase(APITestCase):
    def setUp(self):
        self.ability = Ability.objects.create(name='Powerfull')
        self.pokemon_data = {
            'name': 'PikachuTest',
            'abilities': [{'ability': {'name': 'Powerfull'}}]
        }

    def test_create_pokemon(self):
        headers = {
            'Authorization': 'Token 64e8cd9f0c216bac36c5efe0ccafc22406b39255',
            'Content-Type': 'application/json'
        }
        Pokemon.objects.filter(name='PikachuTest').delete()
        api_response = requests.post('http://localhost:8000/api/pokemon/', json=self.pokemon_data, headers=headers)
        self.assertEqual(api_response.status_code, status.HTTP_200_OK)

    def test_create_existing_pokemon(self):
        Pokemon.objects.create(name='PikachuTest2')
        self.pokemon_data = {
            'name': 'PikachuTest2',
            'abilities': [{'ability': {'name': 'Powerfull'}}]
        }
        headers = {
            'Authorization': 'Token 64e8cd9f0c216bac36c5efe0ccafc22406b39255',
            'Content-Type': 'application/json'
        }
        api_response = requests.post('http://localhost:8000/api/pokemon/', json=self.pokemon_data, headers=headers)

        self.assertEqual(api_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(log_exists('PikachuTest2'))


def log_exists(pokemon_name):
    with open('pokemon_logs.log', 'r') as file:
        for line in file:
            print('line', line)
            log = json.loads(line)
            if log['name'] == pokemon_name:
                return True
    return False
