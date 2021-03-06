run:
	./manage.py runserver

test:
	./manage.py test --keepdb

pep8:
	flake8

sh_p:
	./manage.py shell_plus

migrate:
	./manage.py migrate

load:
	./manage.py load_test_data