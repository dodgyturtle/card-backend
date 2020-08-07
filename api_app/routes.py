from flask import current_app as app
from api_app.database.model import User, Card
from flask import Response, request


@app.route("/v1/user", methods=['POST'])
def user():
    user_data = request.get_json()
    user_info = User(**user_data)
    user_info.save()
    user_id = user_info.id
    return Response(user_id, mimetype="application/json", status=200)

@app.route("/v1/card/<accountid>", methods=['POST'])
def card(accountid):
    card_data = request.get_json()
    user_info = User.objects.get(accountid = str(accountid))
    card_info = Card(**card_data)
    user_info.mycards.append(card_info)
    user_info.save()
    return Response("Ok", mimetype="application/json", status=200)

# @app.route("/user")
# def add_user(index):
#     user_info = User(accountid = str(index))
#     user_info.save()
#     id = user_info.id
#     return {'id': str(id)}, 200
 

@app.route("/get")
def get_info():
    info = User.objects.get(accountid = "789012").to_json()
    return Response(info, mimetype="application/json", status=200)


@app.route("/update", methods=['GET', 'POST'])
def update():
    #card_info = Card(cardname="CardName1", business="Sex", cardnumber="123456789",barcode="987654321", cardcategory="Sales")
    #card_info = {"cardname": "CardName1", "business": "Progsss", "cardnumber": "123456789", "barcode": "987654321", "cardcategory": "Sales"}
    accountid = request.form.get('accountid')
    cardname = request.form.get('cardname')
    user_info = User.objects(accountid = str(accountid), mycards__cardname = str(cardname)).update(set__mycards__S__cardname = 'CardName3')
    #user_info = User.objects(accountid = str(accountid)).first()
    # for info in user_info.mycards:
    #     if info.cardname == 'John':
    #         info.business = 'Sex'
    # user_info.save()
    info = User.objects(accountid = str(accountid), mycards__cardname = str(cardname)).to_json()
    return Response(info, mimetype="application/json", status=200)

