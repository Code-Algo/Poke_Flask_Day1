from . import bp as poke
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from app.models import User, Pokemon

@poke.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        new_poke = Pokemon(user_id = current_user.id)
        new_poke.save()
        flash('Pokemon Captured')
        return redirect(url_for('poke.index'))
    userpokemon = current_user.captured_pokemon()
    return render_template('index.html.j2', userpokemon=userpokemon)

@poke.route('/release_pokemon', methods=['GET', 'POST'])
@login_required
def release_pokemon():
    id = request.arg.get('id')
    pokemon = Pokemon.query.get(id)
    if request.method == 'POST':
        pokemon.release(request.form.get('name'))
        pokemon.save()
        flash('Pokemon Released')
        return render_template('index.html.j2', pokemon=pokemon)

@poke.route('/show_handlers')
def show_handlers():
    users=User.query.filter(User.id != current_user.id).all()
    return render_template('show_user.html.j2', users=users)


