from api_gateway.settings.common import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('HOST')]

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST'), 
        'PORT': os.environ.get('DB_PORT'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS')
    }
}