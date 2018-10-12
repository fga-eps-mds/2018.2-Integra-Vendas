FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD VERSION .

ADD ./api_gateway /code/

RUN pip install --upgrade pip
RUN pip install -r requirements/dev.txt
