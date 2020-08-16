from api_app.database.model import User, Users_Cards

def get_user_info(accountid: str):
    user_info = User.objects.filter(accountid=accountid).first()
    return user_info


def get_card_info(cardid: str):
    card_info = Users_Cards.objects.filter(id=cardid).first()
    return card_info