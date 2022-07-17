Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@Levayaruka 
Levayaruka
/
api_final_yatube
Private
generated from yandex-praktikum/api_final_yatube
Code
Issues
1
Pull requests
Actions
Projects
Security
Insights
Settings
api_final_yatube/README.md
@Levayaruka
Levayaruka Update README.md
Latest commit 0ae5d53 5 minutes ago
 History
 1 contributor
77 lines (76 sloc)  2.22 KB

## Проект «API для Yatube»
### Описание
Проект представляет собой API для публикации и комментирования записей пользователей, с возможность подписываться на интересующих авторов контента. Аутентификация осуществляется по JWT-токену.
### Установка
* Клонируйте репозиторий
```
git clone
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
Для создания, редактирования публикаций или комментариев необходимо использовать полученный JWT-токен в загаловке запроса(Headers)
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
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
