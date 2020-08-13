
from flask import Flask
from flask_mongoengine import MongoEngine

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from test_db import cred

# initializes extensions
db = MongoEngine()
flask_bcrypt = Bcrypt()
jwt = JWTManager()



def create_app():
    application = Flask(__name__)
    application.config['MONGODB_SETTINGS'] = {
        'host': f'mongodb+srv://{cred}@card-db.1amvt.mongodb.net/test?retryWrites=true&w=majority'
    }
    db.init_app(application)
    flask_bcrypt.init_app(application)
    jwt.init_app(application)
    application.config['SECRET_KEY']=cred
    with application.app_context():
        from api_app import routes
    return application
