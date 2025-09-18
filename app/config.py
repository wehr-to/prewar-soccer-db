import os
from dotenv import load_dotenv

# Load .env only in dev/test (ignored by git)
load_dotenv()

class Config:
    """Base config (safe defaults, expects env vars for secrets/prod)"""
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///test.db")
    WTF_CSRF_ENABLED = False  # Useful for automated tests

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Must be set in prod
    SESSION_COOKIE_SECURE = True  # Only over HTTPS
