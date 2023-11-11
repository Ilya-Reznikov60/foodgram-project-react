# Foodgram - Ваш продуктовый помощник
![foodgram-project-react Workflow Status](https://github.com/Ilya-Reznikov60/foodgram-project-react/actions/workflows/main.yml/badge.svg)


[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)

## Описание проекта

«Фудграм» — сайт, на котором пользователи публикуют свои рецепты, добавляют чужие рецепты в избранное и подписываются на публикации других авторов. Пользователям сайта также доступен сервис «Список покупок». Он позволяет создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

Готовый проект можно посмотреть здесь:
[Foodgram](https://foodgramsitework.hopto.org/)

## Данные для админа:
```
Email:reznikov.iluxa@yandex.ru
Password:Rublbudet

```

## Локальный запуск проекта

- Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:

```
git clone https://github.com/Ilya-Reznikov60/foodgram-project-react
```

- Установить и активировать виртуальное окружение

```
python -m venv venv
source /venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Создать файл .env в папке проекта с такими данными:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

- Выполняем миграции:

```
python manage.py migrate
```

- Запускаем тсетовый сервер:

```
python manage.py runserver
```

- Создаём нового супер пользователя:

```
python manage.py createsuperuser
```

- Загрузка статики:

```
python manage.py collectstatic --no-input
```

- Загрузка тестовых данных в виде ингредиентов:

```
python manage.py load_data
```


## Запуск проекта через докер

- в клоннированном репозитории в папке infra выполните следующую команду:

```
docker-compose up -d --build
```

- запустится оркестр контейнеров, проверить их можно командой:

```
docker-compose ps
```

- выполняем миграции:

```
docker-compose exec backend python manage.py migrate
```

- собираем статику:

```
docker-compose exec backend python manage.py collectstatic
docker-compose exec backend python manage.py cp -r /app/static/ . /backend_static/
```

- Грузим тестовые данные:

```
docker-compose exec backend python manage.py load_data   
```

### Вот основные адреса для проверки: 

| Адрес                 | Описание |
|:----------------------|:---------|
| 127.0.0.1            | Главная страница |
| 127.0.0.1/admin/     | Для входа в панель администратора |
| 127.0.0.1/api/docs/  | Описание работы API |


## Настройка CD/CD

1. Файл workflow уже написан. Он находится в директории

    ```bash
    foodgram-project-react/.github/workflows/main.yml
    ```

2. Для адаптации его на своем сервере добавьте секреты в GitHub Actions:

    ```bash
    DOCKER_USERNAME                # имя пользователя в DockerHub
    DOCKER_PASSWORD                # пароль пользователя в DockerHub
    HOST                           # ip_address сервера
    USER                           # имя пользователя
    SSH_KEY                        # приватный ssh-ключ (cat ~/.ssh/id_rsa)
    SSH_PASSPHRASE                 # кодовая фраза (пароль) для ssh-ключа

    TELEGRAM_TO                    # id телеграм-аккаунта (можно узнать у @userinfobot, команда /start)
    TELEGRAM_TOKEN                 # токен бота (получить токен можно у @BotFather, /token, имя бота)
    ```

- Замените в файле docker-compose.ptoduction.yml наименования образов в соответвии с вашим логином на DockerHub
- Далее git add ./ git commit/ git push
Ваш Git Action проведет тесты, соберет образы и отправит их на репозиторий, задеплоит ваш проект на сервер и даже уведомит вас в случае успеха в телеграм.

### Также используйте следующую команду для заполнения БД тестовыми данными:

```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py load_data
```

## Автор
Резников Илья - [GitHub](https://github.com/Ilya-Reznikov60)
