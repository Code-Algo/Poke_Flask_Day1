from . import bp as poke
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user
from app.models import User, Pokemon

@poke.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_poke = Pokemon()
        new_poke.save()
        flash('Pokemon Captured')
        return redirect(url_for('index'))
    userpokemon = current_user.captured_pokemon()
    return render_template('index.html.j2', userpokemon=userpokemon)