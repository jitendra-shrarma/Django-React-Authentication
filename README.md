# Django-Authentication
REST APIs based on Django, to signup/signin, signout and resetpassword. Api to list users based on current user group. 

Only connection to PostgreSQL database remains.

## How to run on your system

### create virtual environment
python -m venv .venv

## activate virtual environment
.venv\Scripts\activate

## upgrade pip tool
python -m pip install --upgrade pip

## install project dependencies in current virtual environment
pip install django
pip install django-rest-framework
pip install djangorestframework_simplejwt
pip install django-crontab
pip install django-environ
pip install psycopg2

## save all project dependencies in requirements.txt
pip freeze > requirements.txt

## start project
django-admin startproject django_auth

## start app in django_auth
python manage.py startapp api

## to run the server
python manage.py runserver

## djangorestframework_simplejwt - this modules needs to be installed
### for JWT authentication, as rest_framework token service
### doesn't work well with requirements.
