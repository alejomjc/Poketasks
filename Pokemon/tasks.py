import random
import requests
from celery import shared_task


@shared_task
def get_random_pokemon(data=None):
    try:
        pokemon_id = random.randint(1, 898)
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
        if response.status_code == 200:
            pokemon_data = response.json()
            headers = {
                'Authorization': 'Token 64e8cd9f0c216bac36c5efe0ccafc22406b39255',
                'Content-Type': 'application/json'
            }
            api_response = requests.post('http://localhost:8000/api/pokemon/', json=pokemon_data, headers=headers)
            if api_response.status_code == 200:
                print(f'Pokemon enviado con éxito a tu API: {pokemon_data["name"]}')
            else:
                print(f'Error al enviar el Pokémon a tu API: {pokemon_data["name"]}')
        else:
            print(f'Error al obtener el Pokémon de la API: {response.status_code}')
    except Exception as e:
        print('error', e)
