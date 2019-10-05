FROM python:3.7.4-alpine

WORKDIR /app

RUN apk --no-cache add \
     bash \
     curl \
     gcc \
     gettext \
     git \
     libffi-dev \
     musl-dev \
     sqlite3

RUN mkdir -p ./app/static && \
    && rm -R ./app/static/* \
    && cd client \
    && RUNPUBLIC_URL=http://127.0.0.1:$PORT/ npm run build
    && mv ./build/** ../app/static

COPY requirements requirements
RUN pip install -r requirements/$DJANGO_ENV.txt

COPY . .
