run:
	python src/manage.py runserver

run_g:
	gunicorn src.config.wsgi:application --bind localhost:8000

reload:
	exit
	pipenv shell

redis:
	celery -A config worker -l INFO
