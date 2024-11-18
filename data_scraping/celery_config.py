from celery import Celery

# Create the Celery app
app = Celery('scraper', broker='redis://redis-19273.c339.eu-west-3-1.ec2.redns.redis-cloud.com:19273/0')

# Optional: Set password if required
app.conf.broker_password = 'fkWeeIquwuNyO0qkj76Nl3NStpph3VKk'

# Optional: set the result backend
# app.conf.result_backend = 'redis://localhost:6379/0'

# Set periodic task schedule (using Celery Beat)
app.conf.beat_schedule = {
    'scrape-jobs-every-10min': {
        'task': 'uci_scraping.scrape_uci_datasets',
        'schedule': 600,  # Every 10 hours
    },
}
app.conf.timezone = 'UTC'

# Start the Celery Worker in terminal 1 with 'celery -A celery_config worker --loglevel=info'
# Start the Celery Beat Scheduler in terminal 2 with 'celery -A celery_config beat --loglevel=info'

