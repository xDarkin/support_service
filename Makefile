run:
	python src/manage.py runserver

run_g:
	gunicorn src.config.wsgi:application --bind localhost:8000
