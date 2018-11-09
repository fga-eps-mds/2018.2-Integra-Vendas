from api_gateway.settings.common import *
from decouple import config

DEBUG = False

SECRET_KEY = config('SECRET_KEY', default='mlcq%tp1&*4k@l*s%nef41*2r6*r+zejfip_dv*0$(&#!jt3pj')

ALLOWED_HOSTS = [config('HOST', default='*')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'HOST': config('DB_HOST', default='db'), 
        'PORT': config('DB_PORT', default='5432'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASS', default='')
    }
}