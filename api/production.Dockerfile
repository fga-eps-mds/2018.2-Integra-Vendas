FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD ./api_gateway /code

RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt

EXPOSE 8000

ENTRYPOINT python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000