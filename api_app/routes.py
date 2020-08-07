from flask import current_app as app
from api_app.database.model import User, Card
from flask import Response, request


# list users
@app.route('/v1/user', methods=['GET'])
def list_users():
    api_info = User.objects.to_json()
    return Response(api_info, mimetype='application/json', status=200)


# add user
@app.route('/v1/user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    user_info = User(**user_data)
    user_info.save()
    api_info = user_info.to_json()
    return Response(api_info, mimetype='application/json', status=200)


# update user
@app.route('/v1/user/<accountid>', methods=['PUT'])
def update_user(accountid: str):
    new_user_data = request.get_json()
    User.objects.get(accountid=str(accountid)).update(**new_user_data)
    api_info = User.objects.get(accountid=str(accountid)).to_json()
    return Response(api_info, mimetype='application/json', status=200)


# delete user
@app.route('/v1/user/<accountid>', methods=['DELETE'])
def delete_user(accountid: str):
    User.objects.get(accountid=str(accountid)).delete()
    return Response('Ok', mimetype='application/json', status=200)


# list card
@app.route('/v1/card/<accountid>', methods=['GET'])
def addcard(accountid: str):
    pass


# add card
@app.route('/v1/card/<accountid>', methods=['POST'])
def add_card(accountid: str):
    card_data = request.get_json()
    user_info = User.objects.get(accountid=str(accountid))
    card_info = Card(**card_data)
    card_info.save()
    user_info.mycards.append(card_info.id)
    user_info.save()
    api_info = card_info.to_json()
    return Response(api_info, mimetype='application/json', status=200)


# update card
@app.route('/v1/card/<cardid>', methods=['PUT'])
def card_update(cardid: str):
    new_card_info = request.get_json()
    print(new_card_info)
    Card.objects.get(id=str(cardid)).update(**new_card_info)
    api_info = Card.objects.get(id=str(cardid)).to_json()
    return Response(api_info, mimetype='application/json', status=200)


# delete card
@app.route('/v1/card/<cardid>', methods=['DELETE'])
def delete_card(cardid: str):
    Card.objects.get(id=str(cardid)).delete()
    return Response('Ok', mimetype='application/json', status=200)


@app.route('/get')
def get_info():
    info = User.objects.get(accountid='123456').to_json()
    return Response(info, mimetype='application/json', status=200)
