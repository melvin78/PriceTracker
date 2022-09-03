FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && apk add --no-cache make g++ bash git openssh postgresql-dev curl supervisor

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./ /usr/src/app
RUN pip install -r requirements.txt

COPY ./utils/supervisor.conf /etc/supervisord.conf



ARG DATABASE_NAME=${DATABASE_NAME}
ARG DATABASE_USERNAME=${DATABASE_USERNAME}
ARG DATABASE_PASSWORD=${DATABASE_PASSWORD}
ARG DATABASE_HOST=${DATABASE_HOST}
ARG DATABASE_PORT=${DATABASE_PORT}
ARG CELERY_BROKER_URL=${CELERY_BROKER_URL}
ARG CELERY_RESULT_BACKEND=${CELERY_RESULT_BACKEND}


CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]
