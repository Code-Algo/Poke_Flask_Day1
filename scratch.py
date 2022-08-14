import requests

url = f"https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

data = response.json()
#print(data['abilities'][1]['ability']['name'])
#print(data['sprites']['other']['home']['front_default'])
def get_pokemon(data):
    new_data=[]
    name = data['name']
    ability = data['abilities'][1]['ability']['name']
    for poke in d:
        poke_dict={
            'name':name,
            
        }
        new_data.append(poke_dict)
    return new_data
#print(get_pokemon(data))
list_data = []
new_data = {
    'name':data['name'],
    'ability': data['abilities'][1]['ability']['name'],
    'defense':data['stats'][2]['base_stat'],
    'attack':data['stats'][1]['base_stat'],
    'HP':data['stats'][0]['base_stat'],
}
print(new_data)

#list_data.append(new_data)
#print(list_data)

  #if not response.ok:
        #error_string = "We had an unexpected error. soz."
        #return render_template('poke_farm.html.j2', error=error_string)