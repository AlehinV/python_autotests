import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'af2d60012bf7ce0550412b5907194cb2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Foxy",
    "photo_id": 38
}
# Создаем нового пекемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text) # Выводим ответ от бэка

message = response_create.json()['message'] # Выводим ответ в формате json 
print(message)

pok_id = response_create.json()['id'] # Создаем переменную pok_id, куда автоматически подставляем полученный id 

body_new_name = {
    "pokemon_id": pok_id,
    "name": "Кицунэ",
    "photo_id": 38
}

response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text) # Выводим ответ от бэка

message = response_new_name.json()['message'] # Выводим ответ в формате json 
print(message) 

body_catch = {
    "pokemon_id": pok_id
}
response_catch_pokemon = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch_pokemon.text) # Выводим ответ от бэка

message = response_catch_pokemon.json()['message'] # Выводим ответ в формате json 
print(message) 