
# "Проект самообучения"

## Задание

    Реализовать функционал самообучения для студентов.
    Создать платформу, которая работает только с авторизованными пользователями.
    На платформе необходимо предусмотреть функционал разделов и материалов.
    Реализовать либо Rest API, либо SSR с использованием Bootstrap.
    Для реализации проекта использовать фреймворк Django.


## Технологии

    - python
    - postgreSQL 

## Фреймворк

    - django = 5.0.3  

## Библиотеки

    - psycopg2-binary = 2.9.9  
    - pillow = 10.2.0"  
    - python-dotenv = 1.0.1  
    - djangorestframework = 3.15.0   
    - djangorestframework-simplejwt = 5.3.1   
    - drf-yasg = 1.21.7   
    - django-cors-headers = 4.3.1  
    - flake8 = 7.0.0


## Виртуальное окружение

    В проекте используется Poetry, все зависимости создаются
    автоматически с помощью файлов 'pyproject.toml' и 'poetry.lock'

## Переменные окружения

Создать файл '.env', добавить в него переменные окружения из '.env.sample'

`SECRET_KEY`,
`POSTGRES_USER`,
`POSTGRES_PASSWORD`,
`POSTGRES_DB`,
`POSTGRES_PORT`,
`POSTGRES_HOST`


## Запуск проекта

Применить миграции командой:

```bash
python3 manage.py migrate
```
Запустить файл users/management/commands/csu.py командой:

```bash
python3 manage.py csu
```
Запустить сервер командой:

```bash
python3 manage.py runserver
```


## Заполнение базы данных

Заполнение базы данных можно осуществить через Django Admin по ссылке, либо в Postman:

[Django Admin](http://localhost:8000/admin/)

    
## Документация 

Документация API доступна после запуска сервера по ссылкам:

[Swagger](http://localhost:8000/swagger/)

[Redoc](http://localhost:8000/redoc/)
