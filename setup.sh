#!/bin/bash

echo "Setting up Superheroes API..."

# Install dependencies
echo "Installing dependencies..."
pipenv install

# Activate virtual environment
echo "Activating virtual environment..."
pipenv shell

# Initialize database
echo "Initializing database..."
flask db init

# Create migrations
echo "Creating migrations..."
flask db migrate -m "Initial migration"

# Apply migrations
echo "Applying migrations..."
flask db upgrade

# Seed the database
echo "Seeding database..."
python seed.py

echo "Setup complete! Run 'python app.py' to start the server."