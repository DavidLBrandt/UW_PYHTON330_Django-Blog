# Flask Mailroom Application Build Notes #

## Virtual Environment Python ##

Setup the virtual environment Python (Windows Powershell)
```
python -m venv venv
```

Activate virtual environment Python (Windows Powershell)
```
.\venv\Scripts\activate.ps1
```

Deactivate virtual environment Python (Windows Powershell)
```
.\venv\Scripts\deactivate.ps1
```

## Virtual Environment Django ##

Setup the virtual environment Django (Command Prompt)
```
mkvirtualenv djangoenv
```

Activate virtual environment Django (Command Prompt)
```
workon djangoenv
```

Deactivate virtual environment Django (Command Prompt)
```
deactivate
```

Django Shell
```
python manage.py shell
```
## Django Environment Setup ##

00) Get list of Django Admin commands
```
django-admin
```

01) Start project to create infrastructure
```
django-admin startproject mysite
```

02) Start server
```
C:\_Python330\Django Blog\django-blog\mysite>python manage.py runserver
```

03) Browse to server
```
http://localhost:8000/
```

04) Build SQLite3 database
```
C:\_Python330\Django Blog\django-blog\mysite>python manage.py makemigrations
C:\_Python330\Django Blog\django-blog\mysite>python manage.py migrate
```

05) Create Super User
```
C:\_Python330\Django Blog\django-blog\mysite>python manage.py createsuperuser
```

06) Create an application (named polling)
```
C:\_Python330\Django Blog\django-blog\mysite>python manage.py startapp polling
```

07) Include application in project by adding polling to installed apps in C:\_Python330\Django Blog\django-blog\mysite\mysite\settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polling',
]
```

Run Django Server (http://localhost:8000/admin/)
```
python manage.py runserver
```

### environment files ###
* **outer *mysite* directory**: this is just a container and can be renamed or moved at will

* **inner *mysite* directory**: this is your project directory. Do not rename it.
* **mysite/__init__.py**: magic file that makes mysite a python package.
* **mysite/settings.py**: file which holds configuration for your project, more soon.
* **mysite/urls.py**: file which holds top-level URL configuration for your project, more soon.
* **mysite/wsgi.py**: binds a wsgi application created from your project to the symbol application
* **mysite/manage.py**: a management control script.

* **inner *polling* directory**: this directory is the polling app and will contain all polling functionality for the site.
* **polling/admin.py**: file that you'll use to register polling models in the Django admin, more soon.
* **polling/migrations.py**: directory for files that tell Django how to build database tables for your polling models.
* **polling/views.py**: file which holds views for the polling app.
* **polling/tests.py**: file which holds tests for the polling app.

## Requirements ##
Install the requirements.txt file to include the required packages
```
pip install -r requirements.txt
```

## Testing ##
Unittest
```
python -m unittest test_main.py
```
Pytest
```
pytest test_main.py
```

## Linting ##
Lint a specific file
```
pylint main.py
```

Lint all files
```
forfiles /M *py /C "cmd /c pylint @file"
```

## Coverage ##
```
coverage run -m unittest test_main.py
coverage report -m
coverage html
```

## Bandit ##
Checks code for security vulnerabilities

## Saftey ##
Checks imported modules for security vulnerabilities

## To Publish to Heroku

All commands to be run from inside the repository directory.
```
$ git init                # Only necessary if this is not already a git repository
$ heroku create
$ git push heroku Development:master  # If you have any changes or files to add, commit them before you push. 
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku run python setup.py
$ heroku open
```
