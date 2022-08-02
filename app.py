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
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if not response.ok:
        error_string = "We had an unexpected error. soz."
        return render_template('poke_farm.html.j2', error=error_string)
    data = []
    new_data = []
    for pokemon in data:
        pokemon_dict={
            "Name":pokemon['name'],
            "Ability":pokemon['ability'][1],
            
        }
    return render_template('poke_farm.html.j2')
