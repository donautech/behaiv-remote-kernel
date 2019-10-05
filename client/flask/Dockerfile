FROM python:3.7.4-alpine

ARG ENVIRONMENT
ARG PORT=${POST}

ENV ENVIRONMENT=${ENVIRONMENT}

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

COPY package.json /app/package.json
RUN npm install

RUN mkdir -p ./static
RUN RUNPUBLIC_URL=http://127.0.0.1:$PORT/ npm run build
#RUN mv ./build/** ./static  Put the build folder in the current directory and remove this line from the comments

COPY requirements requirements
RUN pip install -r requirements/$ENVIRONMENT.txt

COPY . .

ENTRYPOINT /bin/bash /app/client/flask/start.sh $ENVIRONMENT
