# config.py

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")

    # Adjust for PostgreSQL if used
    uri = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/database_dj")

    # Fix Heroku-style URLs for PostgreSQL
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
