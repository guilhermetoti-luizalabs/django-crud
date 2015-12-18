app:
	cd django/django-crud/ && cookiecutter https://github.com/rpedigoni/cookiecutter-django-app

test:
	coverage run --branch --source=django/django-crud  django/django-crud/./manage.py test django/django-crud/ -v 2 --failfast --settings=settings.test
	coverage report --omit=django/django-crud/*/migrations*,django/django-crud/settings/*,django/django-crud/urls.py,django/django-crud/wsgi.py,django/django-crud/manage.py,django/django-crud/*/tests/*,django/django-crud/__init__.py

html:
	coverage html --omit=django/django-crud/*/migrations*,django/django-crud/settings/*,django/django-crud/urls.py,django/django-crud/wsgi.py,django/django-crud/manage.py,django/django-crud/*/tests/*,django/django-crud/__init__.py
	open htmlcov/index.html

doc:
	$(MAKE) -C docs/ html
	open docs/build/html/index.html

deploy:
	fab -f django/fabfile.py deploy

clean:
	rm -f .coverage
	rm -rf htmlcov/
	rm -rf docs/build/
