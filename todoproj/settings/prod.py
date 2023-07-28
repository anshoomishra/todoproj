from .base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

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