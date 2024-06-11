.PHONY: ruff

ruff:
	poetry run ruff check
	poetry run ruff format

runserver: 
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

makemigrations:
	poetry run python manage.py makemigrations
