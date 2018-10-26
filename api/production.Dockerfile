FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

ADD . /code
WORKDIR /code/api_gateway

RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt

RUN apt-get update
RUN apt-get install curl libcurl3 libcurl3-dev -y

EXPOSE 8000

ENTRYPOINT python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 api_gateway.wsgi --log-file -