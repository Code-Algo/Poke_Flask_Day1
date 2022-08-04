from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# initializing
app = Flask(__name__)
app.config.from_object(Config)

## Reg Plugins/texts

# init for database management
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login
login = LoginManager(app)

# Configure some settings
login.login_view = 'login'
login.login_message = 'Please Login First'
login.login_message_category = "warning"




from app import routes, models