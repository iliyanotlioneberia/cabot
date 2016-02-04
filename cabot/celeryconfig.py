import os
from datetime import timedelta

BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_IMPORTS = ('cabot.cabotapp.tasks', )
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERYD_TASK_SOFT_TIME_LIMIT = 120
CELERYD_TASK_TIME_LIMIT = 150
BROKER_POOL_LIMIT = 1000
CELERY_REDIS_MAX_CONNECTIONS = 1000

### Maclin fix
# CELERY_TASK_RESULT_EXPIRES = 10
# CELERY_IGNORE_RESULT = True

CELERYBEAT_SCHEDULE = {
    'run-all-checks': {
        'task': 'cabot.cabotapp.tasks.run_all_checks',
        'schedule': timedelta(seconds=60),
    },
    'update-shifts': {
        'task': 'cabot.cabotapp.tasks.update_shifts',
        'schedule': timedelta(seconds=1800),
    },
    'clean-db': {
        'task': 'cabot.cabotapp.tasks.clean_db',
        'schedule': timedelta(seconds=60*60*24),
    },
    ### deletes 'celery' key in redis every 6 hours
    'delete_celery_cache_redis': {
        'task': 'cabot.cabotapp.tasks.delete_celery_cache_redis',
        'schedule': timedelta(seconds=60*60*1),
    },
}

CELERY_TIMEZONE = 'UTC'
