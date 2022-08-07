from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



## Reg Plugins/texts

# init for database management
db = SQLAlchemy()
migrate = Migrate()

# Login
login = LoginManager()



def create_app(config_class=Config):
    # initializing
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Configure some settings
    login.login_view = 'auth.login'
    login.login_message = 'Please Login First'
    login.login_message_category = "warning"

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from .blueprints.poke import bp as poke_bp
    app.register_blueprint(poke_bp)

    return app

from app import models