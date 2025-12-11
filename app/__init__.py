from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

# Initialize extensions (but don't bind yet)
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app():
    """Flask application factory"""
    app = Flask(__name__)

    # Configuration
  #  app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", "dev_secret_key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///app.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Security settings
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    # Only set Secure in production (breaks localhost if no TLS)
    if not app.debug:
        app.config["SESSION_COOKIE_SECURE"] = True

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
