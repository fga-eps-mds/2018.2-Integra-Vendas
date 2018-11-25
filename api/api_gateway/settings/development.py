from api_gateway.settings.common import *
from api_gateway.file_helper import file_get_contents

SECRET_KEY = 'mlcq%tp1&*4k@l*s%nef41*2r6*r+zejfip_dv*0$(&#!jt3pj'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

VERSION = file_get_contents("../VERSION")
