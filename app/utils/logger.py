import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(app):
    """Configure logging for the given Flask app."""
    log_dir = os.path.join(app.config.get('BASE_DIR'), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'app.log')

    handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=3)
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
