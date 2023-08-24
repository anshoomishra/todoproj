#!/bin/bash

# Wait for PostgreSQL to become available
until psql -h postgres -U $DASHBOARD_POSTGRES_USER -d $DASHBOARD_POSTGRES_DB -c '\l' > /dev/null 2>&1; do
  echo "Waiting for PostgreSQL to become available..."
  sleep 2
done

# Apply database migrations and start the Django application
cd /app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000