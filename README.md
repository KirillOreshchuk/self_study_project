# Проект самообучения


### Задание

Реализовать функционал самообучения для студентов.
Для этого необходимо создать платформу, которая работает только
с авторизованными пользователями. На платформе необходимо
предусмотреть функционал разделов и материалов.
Для каждого материала можно добавить тесты. Управление всеми
сущностями необходимо реализовать через стандартный Django admin.
Проверка ответа на тест осуществляется с помощью отдедльного запроса
на бэкенд. Реализовать либо Rest API, либо SSR с использованием
Bootstrap. Для реализации проекта использовать фреймворк Django.


### Стек технологий

python = 3.10  
django = 5.0.3  
psycopg2-binary = 2.9.9  
pillow = "^10.2.0"   
python-dotenv = 1.0.1  
djangorestframework = 3.15.0   
djangorestframework-simplejwt = 5.3.1   
drf-yasg = 1.21.7   
django-cors-headers = 4.3.1  
flake8 = 7.0.0

### Запуск приложения

1. Создать файл '.env', добавить в него переменные окружения из '.env.sample'
2. Применить миграции командой: 'python3 manage.py migrate'
3. Запустить файл users/management/commands/csu.py командой: 'python3 manage.py csu' - создать суперпользователя 
4. Запустить сервер командой: 'python3 manage.py runserver'