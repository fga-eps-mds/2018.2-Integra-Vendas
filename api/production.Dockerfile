FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD VERSION .
ADD ./api_gateway /code

RUN pip install --upgrade pip
RUN pip install -r requirements/prod.txt

RUN python manage.py makemigrations && \
    python manage.py migrate

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000