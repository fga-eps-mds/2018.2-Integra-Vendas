pip install -r requirements/dev.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test