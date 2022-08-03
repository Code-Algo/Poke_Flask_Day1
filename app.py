from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/dict_pokemon', methods=['GET'])
def dict_pokemon():
    return {"Name":"Pikachu", "Ability":"Static", "Def":"50", "Atk":"50", "HP":"35"}

@app.route('/pokemon', methods =['GET'])
def pokemon():
    flask_pokemon = ['Pikachu', 'Voltorb', "Bulbasaur"]
    return render_template('pokemon.html.j2', pokemon=flask_pokemon)

@app.route('/poke_farm', methods=['GET', 'POST'])
def poke_farm():
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)
        print(response)
        data = response.json()
        new_data = {
        'name':data['name'],
        'ability': data['abilities'][1]['ability']['name'],
        'defence':data['stats'][2]['base_stat'],
        'attack':data['stats'][1]['base_stat'],
        'HP':data['stats'][0]['base_stat'],
        'sprite':data['sprites']['other']['home']['front_default']
        }
        return render_template('poke_farm.html.j2', poke_data=new_data)
    return render_template('poke_farm.html.j2')

    


