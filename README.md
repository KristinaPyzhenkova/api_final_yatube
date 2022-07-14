# Yatube
## Описание проекта.
Данная социальная сеть позволяет пользователю создавать посты и через комментарии - узнавать, что другие пользователи думают о написанном ими. "Подписывтаься" на других пользователей и следить за их публикациями, а если не хочется подписываться - следить анонимно, оставлять свое мнение под чужими постами и много другое.

Как запустить проект:

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```

Примеры.
Необходимо создать учетную запись(иначе, кроме просмотра некоторых категорий - ничего не получится)
POST http://127.0.0.1:8000/auth/users/
Content-Type: application/json

{
    "username": "username",
    "password": "password"
}

POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
    "username": "username",
    "password": "password"
}

Для просмотра и добавления постов(не забывай добавлять токен - если хочешь добавить пост или изменить/удалить ранее написанный):
GET http://127.0.0.1:8000/api/v1/posts/?page=2

POST http://127.0.0.1:8000/api/v1/posts/
Authorization: Bearer ***
Content-Type: application/json

{
    "text": "Test5",
    "group": 1
}

PUT/PUTCH/DELETE http://127.0.0.1:8000/api/v1/posts/1/
Authorization: Bearer ***
Content-Type: application/json

{
    "text": "Test5",
    "group": 1
}

Для просмотра и добавления комментариев(не забывай добавлять токен - если хочешь добавить комментарий или изменить ранее написанный):

POST  http://127.0.0.1:8000/api/v1/posts/1/comments/
Authorization: Bearer ***
Content-Type: application/json
{
    "text": "Test"
}

PUT/PUTCH/DELETE http://127.0.0.1:8000/api/v1/posts/1/comments/1/
Authorization: Bearer ***
Content-Type: application/json

{
    "text": "Test2"
}

Для просмотра или создания подписок (не забудь авторизоваться):
GET http://127.0.0.1:8000/api/v1/follow/

POST http://127.0.0.1:8000/api/v1/follow/
Authorization: Bearer ***
Content-Type: application/json

{
"following": "username"
}
