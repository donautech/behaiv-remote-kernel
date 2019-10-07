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

COPY /app ./app
COPY /config.py ./config.py
COPY /migrations ./migrations
COPY /remote_kernel.py ./remote_kernel.py
COPY /docker/start.sh ./docker/start.sh

ENTRYPOINT /bin/bash /app/docker/start.sh $ENVIRONMENT
