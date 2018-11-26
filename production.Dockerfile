FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

ADD ./api /code
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt

RUN mkdir -p /usr/share/man/man1 && mkdir -p /usr/share/man/man7
RUN apt-get update && apt-get install -f -y postgresql-client curl libcurl3 libcurl3-dev


EXPOSE 8000

ENTRYPOINT python manage.py makemigrations && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 api_gateway.wsgi --log-file -