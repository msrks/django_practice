## Django Practice

create project

```
$ django-admin startproject django_practice
$ cd django_practice/
$ python manage.py runserver
$ python manage.py migrate
```

### 1. create apps (hello world)

```
$ python manage.py startapp posts
```

### 2. create app w/ database

```
$ python manage.py satrtapp diary
$ python manage.py makemigrations diary
$ python manage.py migrate
```

### 3. create superuser for admin

```
$ python manage.py createsuperuser
```
