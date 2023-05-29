FROM python:3.11.2-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install binutils libproj-dev gdal-bin

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt