dev:
	python3 manage.py runserver 8080

venv:
	python3 -m venv venv

deps:
	pip freeze > requirements/base.txt

dbsetup: # applies migrations to db
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations api

restart-compose:
	docker compose down -v && docker compose up --build

compose:
	docker compose up --build
