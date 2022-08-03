from flask import render_template, request
import requests
from app import app
from .forms import LoginForm, RegisterForm


# routes
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm
    return render_template('register.html.j2', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data
        if email in app.config.get("REGISTERED_USERS") and \
            password == app.config.get("REGISTERED_USERS").get(email).get('password'):
            #Login Success
            return f"Login Success Welcome {app.config.get('REGISTERED_USERS').get(email).get('name')}"
        error_string = "Incorrect Email/Password Combo"
        return render_template('login.html.j2', error=error_string, form=form)
    
    return render_template('login.html.j2', form=form)

@app.route('/poke_farm', methods=['GET', 'POST'])
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
