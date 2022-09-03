FROM python:3.10.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk upgrade && apk add --no-cache make g++ bash git openssh postgresql-dev curl

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY ./ /usr/src/app
RUN pip install -r requirements.txt

COPY ./utils/ /usr/src/utils

CMD sh /usr/src/utils/run.sh
