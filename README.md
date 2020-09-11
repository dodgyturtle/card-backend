## Simple backend for Sales-Card Application
### Описание
Простой бэкенд сервер на Python с использованием MongoDB и RestAPI.
Индентификация пользователя проходит по ID.
Есть два режима работы: с регистрацией и без регистрации.
Без регистрации:
Авторизация по токену. Срок жизни токена не ограничен. Повторное получение токена **невозможно**.
С регистрацией:
Для регистрации необходимо передать серверу ID, EMail и пароль.
Срок жизни токена не ограничен.
Для повторного получения токена необходимо передать ID, EMail и пароль.
Описание API на Swagger:  https://app.swaggerhub.com/apis/dumbturtle/card-back-api/0.1

### Требования

 - Python 3.7+
 - MongoDB
### Структура базы данных

**Пользователь:**
- ID пользователя: accountid = db.StringField(required=True, unique=True)
- Имя: name = db.StringField()
- Фамилия: surname = db.StringField()
- Дата рождения: birthdate = db.StringField()
- Пол: gender = db.StringField()
- Электронный адрес: email = db.StringField()
- Пароль: password = db.BinaryField()
- Список карт: mycards = db.ListField()
		
**Скидочная карта:**
- ID пользователя:accountid = db.StringField(required=True, unique=False)
- Название карты: cardname = db.StringField(required=True, unique=False)
- Направление: business = db.StringField()
- Номер карты: cardnumber = db.StringField(required=True, unique=False)
- Баркод: barcode = db.StringField(required=True, unique=False)
- Категория: cardcategory = db.StringField()