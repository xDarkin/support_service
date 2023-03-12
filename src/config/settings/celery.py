from os import getenv

CELERY_BROKER_URL = getenv("REDIS_URL", default="redis://redis:6379/0")
