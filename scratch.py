import requests

url = f"https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

name = response.json()['name']
ability = response.json()['abilities'][1]
print(ability)