from app import db, login
from flask_login import UserMixin # this is only for the user model
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash

handler = db.Table("handler",
    db.Column("pokemon_id", db.Integer, db.ForeignKey("pokemon.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")))

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, index=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime, default=dt.utcnow)
    icon = db.Column(db.Integer)
    pokemon = db.relationship('Pokemon', secondary=handler, backref='handler',lazy='dynamic')

    # should return a unique identifying string
    def __repr__(self):
        return f'<User: {self.email} | {self.id}>'

    # Human readable repr
    def __str__(self):
        return f'<User: {self.email} | {self.first_name} {self.last_name}>'

    # salts and hashes on our passwords make them hard to steal
    def hash_password(self, original_password):
        return generate_password_hash(original_password)

    # compares the user password to the password provided in the login form
    def check_hashed_password(self, login_password):
        return check_password_hash(self.password, login_password)

    def save(self):
        db.session.add(self) # add the user to the session
        db.session.commit() # save the stuff in the session to the database

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    def from_dict(self, data):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=self.hash_password(data['password'])
        self.icon=data['icon']

    def get_icon_url(self):
        return f"https://avatars.dicebear.com/api/adventurer-neutral/{self.icon}.svg"

    # Check to see if pokemon is already on poke team
    def is_captured(self, pokemon_to_check):
        return pokemon_to_check in self.pokemon

    def capture_pokemon(self, pokemon_to_capture):
        if not self.is_captured(pokemon_to_capture):
            self.pokemon.append(pokemon_to_capture)
            db.session.commit()

    def release_pokemon(self, pokemon_to_release):
        if self.is_captured(pokemon_to_release):
           self.pokemon.remove(pokemon_to_release)
           db.session.commit()

    def captured_pokemon(self):
        # get my own poke
        return self.pokemon.all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    # SELECT * FOM user WHERE id

class Pokemon(db.Model):
    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ability = db.Column(db.String)
    attack = db.Column(db.String)
    defense = db.Column(db.String)
    hp = db.Column(db.String)
    url = db.Column(db.String)

    def __repr__(self):
        return f'<Pokemon: {self.id} | {self.name}'

    def save(self):
        db.session.add(self) # add the user to the session
        db.session.commit() # save the stuff in the session to the database

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, data):
        self.name=data['name']
        self.ability=data['ability']
        self.attack=data['attack']
        self.defense=['defense']
        self.hp=data['HP']
        self.url=data['sprite']

    