# first file in the project that runs whenever we run the project 
# It deal with everything that has to setup only once (setting up instance, setting up database, logging feature for every instance )


# Registering a blueprint in Flask means integrating a modular component into the main Flask application. Blueprints allow you to organize your Flask application into smaller, reusable modules, each containing routes, templates, static files, and other components related to a specific feature or section of your application.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# initializing database instance 
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)


    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # inititalize our app database 
    db.init_app(app)

    login_manager= LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # user loader searches for the specific user based on the user ID 
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # . represents the current structure 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app