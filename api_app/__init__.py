
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initializes extensions
#db = SQLAlchemy()


def create_app():
    application = Flask(__name__)
    
    #db.init_app(app)
    with application.app_context():
        from api_app import routes

    return application
