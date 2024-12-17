import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '87c0336dfacc25856a5cb5ef8288b6fb'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12051'

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainerid():
    response_treinerid = requests.get(url=f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_treinerid.json()['data'][0]['trainer_id'] == '12051'