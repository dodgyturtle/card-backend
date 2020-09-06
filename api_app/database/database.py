from api_app.database.model import User, Users_Cards
from bson import ObjectId

def get_user_info(accountid: str):
    user_info = User.objects.filter(accountid=accountid).first()
    return user_info

def password_check(accountid: str):
    user_info = User.objects.filter(accountid=accountid).first()
    if user_info.password:
        return True
    return False


def get_card_info(cardid: str):
    if not ObjectId.is_valid(cardid):
        return None
    card_info = Users_Cards.objects.filter(id=cardid).first()
    return card_info