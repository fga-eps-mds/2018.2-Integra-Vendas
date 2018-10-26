FROM python:3.5.6-slim-stretch
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD VERSION .

ADD ./api_gateway /code/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt

RUN apt-get update
RUN apt-get install curl libcurl3 libcurl3-dev -y