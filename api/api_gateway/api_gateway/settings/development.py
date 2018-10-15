from api_gateway.settings.common import *

SECRET_KEY = 'mlcq%tp1&*4k@l*s%nef41*2r6*r+zejfip_dv*0$(&#!jt3pj'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

