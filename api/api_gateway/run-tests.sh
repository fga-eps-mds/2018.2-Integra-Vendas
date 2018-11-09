set -e

pip install -r requirements/dev.txt
python manage.py makemigrations
python manage.py migrate

rm -rf .coverage
coverage run manage.py test
coverage report || true