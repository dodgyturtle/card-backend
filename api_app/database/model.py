from api_app import db


class Users_Cards(db.Document):
    accountid = db.StringField(required=True, unique=False)
    cardname = db.StringField(required=True, unique=False)
    business = db.StringField()
    cardnumber = db.StringField(required=True, unique=False)
    barcode = db.StringField(required=True, unique=False)
    cardcategory = db.StringField()


class User(db.Document):
    accountid = db.StringField(required=True, unique=True)
    name = db.StringField(required=True)
    surname = db.StringField()
    birthdate = db.StringField()
    gender = db.StringField()
    email = db.StringField(required=True)
    mycards = db.ListField()
