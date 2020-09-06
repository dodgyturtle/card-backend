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
from api_app.database.database import get_card_info, get_user_info, password_check
from api_app.database.model import User, Users_Cards
from api_app.return_handlers import response_processing


# info user
@app.route('/v1/user/<accountid>', methods=['GET'])
@jwt_required
def info_user(accountid: str):
    user_info = get_user_info(accountid)
    if not user_info:
        return jsonify({'message': f'User {accountid} is not exist!'}), 403
    user_info.password = ''.encode()
    api_info = user_info.to_json()
    return jsonify({"data": api_info}), 200


# add user
@app.route('/v1/user', methods=['POST'])
def add_user():
    user_info_from_request = request.get_json()
    user_accountid = user_info_from_request.get('accountid')
    if get_user_info(user_accountid):
        return jsonify({'message': f'User {user_accountid} alredy exist!'}), 403
    user_info = User(**user_info_from_request)
    if user_info.password and user_info.email:
        user_info.password = flask_bcrypt.generate_password_hash(user_info.password)
    access_token = create_access_token(identity=user_info.accountid, expires_delta=False)
    user_info.save()
    if password_check(user_accountid):
        answer_code = '02'
    else:
        answer_code = '01'
    api_reply = response_processing(answer_code, {'token': access_token})
    return jsonify(api_reply), 200


# update user
@app.route('/v1/user', methods=['PUT'])
@jwt_required
def update_user():
    user_info_from_request = request.get_json()
    accountid = user_info_from_request.get('accountid')
    user_info = get_user_info(accountid)
    if not user_info:
        return jsonify({'message': f'User {accountid} is not exist!'}), 403
    user_info.update(**user_info_from_request)
    api_info = get_user_info(accountid).to_json()
    return jsonify({'data': api_info}), 200

#resend token
@app.route('/v1/token/<accountid>', methods=['GET'])
def resend_token_user(accountid: str):
    authorization_info = request.authorization
    user_info = get_user_info(accountid)
    if not user_info:
        return jsonify({'message': f'User {accountid} is not exist!'}), 403 
    if (authorization_info.username == user_info.email) and (
            flask_bcrypt.check_password_hash(
                user_info.password, authorization_info.password)):
        access_token = create_access_token(identity=user_info.accountid, expires_delta=False)
        return jsonify({'token': access_token}), 200
    return jsonify({'message': 'Invalid username or password'}), 401
    



# delete user
@app.route('/v1/user/<accountid>', methods=['DELETE'])
@jwt_required
def delete_user(accountid: str):
    user_info = get_user_info(accountid)
    if not user_info:
        return jsonify({'message': f'User {accountid} is not exist!'}), 403
    [Users_Cards.objects.get(id=user_card).delete() for user_card in user_info.mycards]
    user_info.delete()
    return jsonify({'message': f'User {accountid} deleted!'}), 200


# list card
@app.route('/v1/card/<accountid>', methods=['GET'])
@jwt_required
def list_cards(accountid: str):
    if not get_user_info(accountid):
        return jsonify({'message': f'User {accountid} is not exist!'}), 403
    api_info = Users_Cards.objects(accountid=accountid).to_json()
    return jsonify({'data': api_info}), 200


# add card
@app.route('/v1/card', methods=['POST'])
@jwt_required
def add_card():
    card_info_from_request = request.get_json()
    accountid = card_info_from_request.get('accountid')
    user_info = get_user_info(accountid)
    if not user_info:
        return jsonify({'message': f'User {accountid} is not exist!'}), 403
    card_info = Users_Cards(**card_info_from_request)
    card_info.accountid = str(accountid)
    card_info.save()
    user_info.mycards.append(card_info.id)
    user_info.save()
    api_info = card_info.to_json()
    return jsonify({'data': api_info}), 200


# update card
@app.route('/v1/card', methods=['PUT'])
@jwt_required
def card_update():
    card_info_from_request = request.get_json()
    cardid = card_info_from_request.get('id')
    card_info = get_card_info(cardid)
    if not card_info:
        return jsonify({'message': f'Card {cardid} is not exist!'}), 403
    card_info.update(**card_info_from_request)
    api_info = get_card_info(cardid).to_json()
    return jsonify({'data': api_info}), 200


# delete card
@app.route('/v1/card/<cardid>', methods=['DELETE'])
@jwt_required
def delete_card(cardid: str):
    card_info = get_card_info(cardid)
    if not card_info:
        return jsonify({'message': f'Card {cardid} is not exist!'}), 403
    User.objects(accountid = card_info.accountid).update(pull__mycards=ObjectId(cardid))
    card_info.delete()
    return jsonify({'message': f'Card {cardid} deleted!'}), 200
