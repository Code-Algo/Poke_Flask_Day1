from . import bp as poke
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import User, Pokemon

@poke.route('/', methods=['GET'])
@login_required
def index():
    userpokemon = current_user.pokemon.all()
    return render_template('index.html.j2', userpokemon=userpokemon)

@poke.route('/choose_pokemon')
def pokedex():
    pokemon = Pokemon.query.all()
    return render_template('choose_pokemon.html.j2', pokemon=pokemon)

@poke.route('/capture_pokemon/<int:id>', methods=['GET'])
@login_required
def capture_pokemon(id):
    pokemon = Pokemon.query.get(id)
    current_user.capture_pokemon(pokemon)
    current_user.save()
    flash('Pokemon Captured', 'success')
    return redirect(url_for('main.choose_pokemon', pokemon=pokemon))

@poke.route('/release_pokemon/<int:id>', methods=['GET'])
@login_required
def release_pokemon(id):
    pokemon = Pokemon.query.get(id)
    current_user.release_pokemon(pokemon)
    current_user.save()
    flash('Pokemon Released', 'success')
    return render_template(url_for('main.choose_pokemon', pokemon=pokemon))

@poke.route('/show_handlers')
def show_handlers():
    users=User.query.filter(User.id != current_user.id).all()
    return render_template('show_handler.html.j2', users=users)


