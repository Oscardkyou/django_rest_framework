[![Мой проект](https://img.shields.io/badge/Мой%20проект-ваш_текст-<цвет>.svg)](ссылка_на_проект)

Это пример проекта Django, использующего Django REST Framework для создания API. Проект включает три различных API для управления различными моделями данных.
Установка и настройка проекта

    Клонируйте репозиторий на свою локальную машину:

    bash

git clone git@github.com:Oscardkyou/django_rest_framework.git

Перейдите в каталог проекта:

bash

cd django_rest_framework

Установите зависимости проекта:

pip install -r requirements.txt

Выполните миграции базы данных:

python manage.py migrate

Запустите сервер разработки:

    python manage.py runserver

Теперь ваш проект готов к использованию.
API Endpoints
API 1: Users API

    Endpoint: /api/users/
    Методы: GET, POST
    Описание: Этот API позволяет получать список пользователей или создавать новых пользователей.

API 2: Posts API

    Endpoint: /api/posts/
    Методы: GET, POST
    Описание: Этот API позволяет получать список постов или создавать новые посты.

API 3: Comments API

    Endpoint: /api/comments/
    Методы: GET, POST
    Описание: Этот API позволяет получать список комментариев или создавать новые комментарии.

Дополнительная информация

Для работы с API, вы можете использовать инструменты, такие как Swagger или Postman, чтобы легко тестировать и взаимодействовать с API эндпоинтами.

Если вам нужна более подробная информация о каждом API эндпоинте или о моделях данных, пожалуйста, обратитесь к документации Django REST Framework, включенной в проект.

Примечание: Это простое описание проекта и API, и оно может быть дополнено или изменено в зависимости от требований и особенностей вашего проекта.
