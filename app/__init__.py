"""Application factory for the Flask app."""

from flask import Flask
from .config import Config
from .utils.logger import configure_logging

def create_app():
    """Create and configure the Flask application."""
    # Serve static files from the top-level ``static`` directory
    app = Flask(__name__, static_folder="../static", static_url_path="/static")
    app.config.from_object(Config)

    configure_logging(app)

    # Register blueprints
    from .blueprints.uploads import bp as uploads_bp
    app.register_blueprint(uploads_bp)

    # Optional API blueprint
    from .blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
