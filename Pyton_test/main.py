import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '87c0336dfacc25856a5cb5ef8288b6fb'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "generate",
    "photo_id": 1
}
response_create = requests.post(url= f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.json())
pokcreate=response_create.json()['id']
print(pokcreate)

body_put= {
    "pokemon_id": pokcreate,
    "name": "generate",
    "photo_id": 2
}
response_put = requests.put(url= f'{URL}/pokemons', headers=HEADER, json=body_put)
print(response_put.text)

body_pokeboll={
    "pokemon_id": pokcreate
}
response_pokeboll = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeboll )
print(response_pokeboll.text)