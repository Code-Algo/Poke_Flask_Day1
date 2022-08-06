from flask import render_template, request
import requests
from flask_login import login_required
from . import bp as main


# routes
@main.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@main.route('/dict_pokemon', methods=['GET'])
def dict_pokemon():
    return {"Name":"Pikachu", "Ability":"Static", "Def":"50", "Atk":"50", "HP":"35"}

@main.route('/choose_pokemon', methods =['GET', 'POST'])
@login_required
def choose_pokemon():
    form = ChooseForm()
    if request.method == 'POST':
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        response = requests.get(url)
        if not response.ok:
            error_string = "Couldn't Find That Pokemon. Spelling, Perhaps?"
            return render_template('pokemon.html.j2', error=error_string)

        data = response.json()
        new_data = {
            'name':data['name'],
            'ability': data['abilities'][1]['ability']['name'],
            'defence':data['stats'][2]['base_stat'],
            'attack':data['stats'][1]['base_stat'],
            'HP':data['stats'][0]['base_stat'],
            'sprite':data['sprites']['other']['home']['front_default']
        }

        new_poke = Pokemon()
        new_poke.from_dict(new_data)
        new_poke.save_poke()


        @main.route('/catch_pokemon', methods=['GET', 'POST'])
@login_required
def catch_pokemon():
    form = PokemonForm()
    if request.method == 'POST':
        # poke_name = form.poke_name.data.lower()
        # print(poke_name)
        name = request.form.get('name')
        url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
        response = requests.get(url)
        if not response.ok:
            error_string = "Invalid selection, try again."
            return render_template('pokemon.html.j2', error=error_string)
        
        data = response.json()
        poke_dict={
            "name": data['name'].lower(),
            "ability":data['abilities'][0]["ability"]["name"].lower(),
            "base_experience":data['base_experience'],
            "attack_base_stat": data['stats'][1]['base_stat'],
            "hp_base_stat":data['stats'][0]['base_stat'],
            "defense_stat":data['stats'][2]["base_stat"],
            "photo":data['sprites']['other']['home']["front_default"],
            "user_id": current_user.id
        }
        

        new_pokemon = Pokemon()
        new_pokemon.from_dict(poke_dict)
        new_pokemon.save_poke()

        poke2 = Pokemon.query.filter_by(name=name.lower()).first()
        print(poke2)
        print(type(poke2))
        print(current_user)
        current_user.pokemon.append(poke2)
        print(current_user.pokemon.all())
        current_user.save()
        poke2.save_poke()

        print(current_user.pokemon)
        
        current_user


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
