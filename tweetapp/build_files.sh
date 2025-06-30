#!/bin/bash

# Build the project
echo "Building the project..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Make migrations
echo "Making migrations..."
python manage.py makemigrations --noinput

# Apply migrations
echo "Applying migrations..."
python manage.py migrate --noinput 