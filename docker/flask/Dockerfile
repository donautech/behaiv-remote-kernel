FROM python:3.7.4-alpine

ARG ENVIRONMENT
ARG PORT=${POST}

ENV ENVIRONMENT=${ENVIRONMENT}
CMD ./client_dev.sh

WORKDIR /app

RUN apk --no-cache add \
     bash \
     curl \
     nodejs \
     npm \
     gcc \
     gettext \
     git \
     libffi-dev \
     musl-dev \
     sqlite

COPY requirements requirements
RUN pip install -r requirements/$ENVIRONMENT.txt

COPY . .

ENTRYPOINT /bin/bash /app/docker/flask/start.sh $ENVIRONMENT
