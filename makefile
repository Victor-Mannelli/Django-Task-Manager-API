dev:
	python3 manage.py runserver 8080

venv:
	python3 -m venv venv

deps:
	pip freeze > requirements.txt

dbsetup: # applies migrations to db
	python3 manage.py migrate 

migrations:
	python3 manage.py makemigrations task_manager

restart-compose:
	docker compose down -v && docker compose up --build

compose:
	docker compose up --build

superuser:
	python3 manage.py createsuperuser