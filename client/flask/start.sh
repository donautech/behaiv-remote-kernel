#!/usr/bin/env bash

if [[ $1 == "development" ]]; then
  FLASK_DEBUG=1 flask run
else
  # For production environment
  python -m flask run
fi
