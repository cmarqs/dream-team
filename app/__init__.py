# third-party imports
from flask import Flask  # most important
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    """
    Given a configuration name, loads the correct 
    configuration from the config.py
    :param config_name: The configuration name to load the configuration
    :return: The app to be initialized
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    """
    Configurations of the flask-login, in which, if user tries to access a 
    page that they are not authorized to, it will redirect to the specific
    view and display the message below on the route auth.login
    """
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    """
    Migrations setting up.
    This object "migrate" will allow us to run migrations using Flask-Migrate.
    We also have imported the models from the app package.
    """
    migrate = Migrate(app, db)
    Bootstrap(app)

    """
    Import the models to be used in the application
    """
    from app import models

    """
    Configuring the blueprints of each package on the app
    """
    from .admin import admin as admin_blueprint
    # This url_prefix means that all the views for this blueprint will be
    # accessed in the browser with the url prefix admin.
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
