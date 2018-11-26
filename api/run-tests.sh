#!/bin/bash
set -e

pip install -r requirements/dev.txt
python manage.py makemigrations
python manage.py migrate

rm -rf .coverage
coverage run manage.py test
coverage report || true

if [ -f codecov_token ]; then
    echo " ✓ Reading file codecov_token"
    CODECOV_TOKEN=$(cat codecov_token)
fi

if [ ! -z "$CODECOV_TOKEN" ]; then
    echo "Publishing Codecov..."
    codecov -t ${CODECOV_TOKEN}
fi