#!/usr/bin/env bash
flask db upgrade
if [[ $1 == "development" ]]; then
  FLASK_DEBUG=1 flask run --host=0.0.0.0
else
  # For production environment
  python -m flask run --host=0.0.0.0
fi
