django-crud
===========

Installation
------------

Create a virtualenv (use ``virtualenvwrapper``): ::

    mkvirtualenv django-crud


Install requirements via ``pip``: ::

    pip install django/requirements/development.txt


Make migrations: ::

    # on django/django-crud
    ./manage.py makemigrations


Create database tables: ::

    # on django/django-crud
    ./manage.py syncdb


Run the project: ::

    # on django/django-crud
    ./manage.py runserver


Tests
-----

To run the test suite, execute: ::

    make test


To show coverage details (in HTML), use: ::

    make test html
