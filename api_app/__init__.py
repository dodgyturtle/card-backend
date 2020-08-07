
from flask import Flask
from flask_mongoengine import MongoEngine
from test_db import cred

# initializes extensions
db = MongoEngine()


def create_app():
    application = Flask(__name__)
    application.config['MONGODB_SETTINGS'] = {
        'host': f'mongodb+srv://{cred}@card-db.1amvt.mongodb.net/test?retryWrites=true&w=majority'
    }
    db.init_app(application)
    with application.app_context():
        from api_app import routes
    return application
