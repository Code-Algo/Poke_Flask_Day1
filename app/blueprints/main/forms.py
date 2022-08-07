from click import password_option
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
import random
from jinja2.utils import markupsafe

class ChooseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])