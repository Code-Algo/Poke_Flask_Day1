from flask import Blueprint

bp = Blueprint('poke', __name__,url_prefix='')

from . import routes