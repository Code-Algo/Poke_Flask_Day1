from flask import render_template, request
import requests
from flask_login import login_required
from . import bp as main
from . forms import ChooseForm


# routes
@main.route('/dict_pokemon', methods=['GET'])
def dict_pokemon():
    return {"Name":"Pikachu", "Ability":"Static", "Def":"50", "Atk":"50", "HP":"35"}

@main.route('/choose_pokemon', methods =['GET', 'POST'])
@login_required
def choose_pokemon():
    form = ChooseForm()
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}/'
        response = requests.get(url)
        if not response.ok:
            error_string = "Couldn't Find That Pokemon! Spelling, Perhaps?"
            return render_template('choose_pokemon.html.j2', error=error_string)
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
        return render_template('choose_pokemon.html.j2', poke_data=new_data)
    return render_template('choose_pokemon.html.j2')



@main.route('/poke_farm', methods=['GET', 'POST'])
def poke_farm():
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        response = requests.get(url)
        if not response.ok:
            error_string = "We had an Unexpected Error. Check Spelling."
            return render_template('poke_farm.html.j2', error=error_string)
        if not response.json():
            error_string = "Pokemon Not Found. Check Spelling"
            return render_template('poke_farm.html.j2', error=error_string)
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
