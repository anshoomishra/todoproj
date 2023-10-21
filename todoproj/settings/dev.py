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

    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "postgres",
    #     "USER": "postgres",
    #     "PASSWORD": "postgres",
    #     "HOST": "db",  # set in docker-compose.yml
    #     "PORT": 5432,  # default postgres port
    # }
}
CERT_PATH = CERT
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'  # Use the SES SMTP endpoint for your region
EMAIL_PORT = 2465  # Use the appropriate port for SES
EMAIL_HOST_USER = 'AKIARS7EPJ3V6WYO5BW3'
EMAIL_HOST_PASSWORD = 'BAJzFaWj7QretmFjH3leoOCQOV7Rg/jR8uXWDVO2Yokz'
EMAIL_USE_TSL = True
EMAIL_SSL_CA_BUNDLE = CERT_PATH
# (Optional) Set the default 'from' email address
DEFAULT_FROM_EMAIL = 'anshum45@gmail.com'
# from django.core.mail import send_mail

# send_mail("Test Subject","Test Message","anshum45@gmail.com",["anshoomihsra.in@gmailc.com"])