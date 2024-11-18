from celery import Celery

# Create the Celery app
app = Celery('scraper', broker='redis://localhost:6379/0')

# Optional: set the result backend
app.conf.result_backend = 'redis://localhost:6379/0'
