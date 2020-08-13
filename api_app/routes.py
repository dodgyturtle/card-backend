import json

from bson.objectid import ObjectId
from flask import Response
from flask import current_app as app
from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                get_jwt_identity, jwt_refresh_token_required,
                                jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

from api_app import flask_bcrypt
from api_app.database.model import User, Users_Cards


# list users
@app.route('/v1/user', methods=['GET'])
def list_users():
    api_info = User.objects.to_json()
    return Response(api_info, mimetype='application/json', status=200)


# add user
@app.route('/v1/user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if User.objects.filter(accountid=user_data.get('accountid')):
        return jsonify({'message': f'User {user_data.get("accountid")} alredy exist!'}), 403
    user_info = User(**user_data)
    if user_info.password:
        user_info.password = flask_bcrypt.generate_password_hash(user_info.password)
        access_token = create_access_token(identity=user_info.accountid)
        user_info.save()
        return jsonify({'token': access_token}), 200
    user_info.save()
    api_info = user_info.to_json()
    return jsonify({'massage': f'Unauthorized user {user_data.get("accountid")} created!'}), 200

# update user
@app.route('/v1/user/<accountid>', methods=['PUT'])
def update_user(accountid: str):
    user_new_data = request.get_json()
    User.objects.get(accountid=str(accountid)).update(**user_new_data)
    api_info = User.objects.get(accountid=str(accountid)).to_json()
    return Response(api_info, mimetype='application/json', status=200)


# delete user
@app.route('/v1/user/<accountid>', methods=['DELETE'])
def delete_user(accountid: str):
    user_info = User.objects.get(accountid=str(accountid))
    [Users_Cards.objects.get(id=user_card).delete() for user_card in user_info.mycards]
    user_info.delete()
    return Response('Ok', mimetype='application/json', status=200)


# list card
@app.route('/v1/card/<accountid>', methods=['GET'])
@jwt_required
def list_cards(accountid: str):
    api_info = Users_Cards.objects(accountid=str(accountid)).to_json()
    return Response(api_info, mimetype='application/json', status=200)


# add card
@app.route('/v1/card/<accountid>', methods=['POST'])
def add_card(accountid: str):
    card_data = request.get_json()
    user_info = User.objects.get(accountid=str(accountid))
    card_info = Users_Cards(**card_data)
    card_info.accountid = str(accountid)
    card_info.save()
    user_info.mycards.append(card_info.id)
    user_info.save()
    api_info = card_info.to_json()
    return Response(api_info, mimetype='application/json', status=200)


# update card
@app.route('/v1/card/<cardid>', methods=['PUT'])
def card_update(cardid: str):
    new_card_info = request.get_json()
    Users_Cards.objects.get(id=str(cardid)).update(**new_card_info)
    api_info = Users_Cards.objects.get(id=str(cardid)).to_json()
    return Response(api_info, mimetype='application/json', status=200)


# delete card
@app.route('/v1/card/<cardid>', methods=['DELETE'])
def delete_card(cardid: str):
    card_info = Users_Cards.objects.get(id=str(cardid))
    User.objects(accountid = card_info.accountid).update(pull__mycards=ObjectId(str(cardid)))
    card_info.delete()
    return Response('Ok', mimetype='application/json', status=200)
