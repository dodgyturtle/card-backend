
import logging

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

import test_db

# initializes extensions
db = MongoEngine()
flask_bcrypt = Bcrypt()
jwt = JWTManager()


def create_app():
    application = Flask(__name__)
    application.config['MONGODB_SETTINGS'] = {
        'host': f'mongodb+srv://{test_db.CRED}@card-db.1amvt.mongodb.net/test?retryWrites=true&w=majority'
    }
    db.init_app(application)
    flask_bcrypt.init_app(application)
    jwt.init_app(application)
    application.config['SECRET_KEY'] = test_db.CRED
    with application.app_context():
        from api_app import routes
    return application
