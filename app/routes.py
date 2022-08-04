from flask import redirect, render_template, request, url_for, flash
import requests
from app import app
from .forms import LoginForm, RegisterForm
from .models import User
from flask_login import login_user, login_required, logout_user


# routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/dict_pokemon', methods=['GET'])
def dict_pokemon():
    return {"Name":"Pikachu", "Ability":"Static", "Def":"50", "Atk":"50", "HP":"35"}

@app.route('/pokemon', methods =['GET'])
@login_required
def pokemon():
    flask_pokemon = ['Pikachu', 'Voltorb', "Bulbasaur"]
    return render_template('pokemon.html.j2', pokemon=flask_pokemon)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        try:
            new_user_data={
                "first_name":form.first_name.data.title(),
                "last_name":form.last_name.data.title(),
                "email":form.email.data.lower(),
                "password":form.password.data
            }
            # Create an Empty User
            new_user_object = User()

            #build our user from the form data
            new_user_object.from_dict(new_user_data)

            #save new user to the database
            new_user_object.save()
        except:
            # flash user
            flash("An Unexpected Error Occured", "danger")
            return render_template('register.html.j2', form=form)
        # Flash user here telling you have been registered
        flash("Registration Successful", "success")
        return redirect(url_for('login'))

    return render_template('register.html.j2', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data.lower()
        password = form.password.data

        u = User.query.filter_by(email=email).first()

        if u and u.check_hashed_password(password):
            #Login Success!!!!!
            # Flash User
            flash("Login Successful", "success")
            login_user(u)
            return redirect(url_for('index'))
        #flash this
        flash("Incorrect Email/Password Combo", "warning")
        return render_template('login.html.j2', form=form)
    
    return render_template('login.html.j2', form=form)

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    # flash user say goodbye
    flash("Logout Successful", "primary")
    return redirect(url_for('index'))

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
