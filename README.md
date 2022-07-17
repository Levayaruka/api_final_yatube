## Проект «API для Yatube»
### Описание
Проект представляет собой API для публикации и комментирования записей пользователей, с возможность подписываться на интересующих авторов контента. Аутентификация осуществляется по JWT-токену.
### Установка
* Клонируйте репозиторий
```
git clone https://github.com/Levayaruka/api_final_yatube.git
```
* Перейдите в него с помощью встроенной командной строки или предустановленной в IDE(VSCode,PyCharm и другие).
```
cd api_final_yatube/
```
* Установите и активируйте виртуальное окружение(Версия python не ниже 3.7):
```
python -m venv venv
source venv/Scripts/activate
```
* Установите библиотеки из файла requirements.txt
```
pip install -r requirements.txt
```
Запустите проект находясь в каталоге ...api_final_yatube/yatube_api
```
python manage.py runserver
```
### Примеры использования
Полный список эндпоинтов доступен по адресу http://127.0.0.1:8000/redoc

* POST-запрос на получения JWT-токена
```
api/v1/jwt/create/
```
Тело запроса(body)
```
{
  "username": "string",
  "password": "string"
}
```
Ответ(response)
```
{
  "refresh": "string",
  "access": "string"
}
```
Для создания, редактирования публикаций или комментариев, просмотра подписок необходимо использовать полученный JWT-токен в загаловке запроса(Headers)
```
Authorization: Bearer {ваш токен}
```
* POST-запрос для создания публикации
```
api/v1/posts/
```
Заголовок(Headers)
```
Authorization: Bearer {ваш токен}
```
Тело запроса(body)
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ(response)
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
