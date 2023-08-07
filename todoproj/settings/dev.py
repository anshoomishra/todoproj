from .base import *

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0','localhost']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DASHBOARD_POSTGRES_DB'],
        'USER': os.environ['DASHBOARD_POSTGRES_USER'],
        'PASSWORD': os.environ['DASHBOARD_POSTGRES_PASSWORD'],
        'HOST': os.environ['DASHBOARD_POSTGRES_IP'],
        'PORT': os.environ['DASHBOARD_POSTGRES_PORT']
    }
}