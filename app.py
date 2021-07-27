from flask import Flask
from config import DevelopmentConfig, ProductionConfig
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask


def create_app(configuration=DevelopmentConfig):
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(configuration)

    file_handler = RotatingFileHandler(
        'app.log', maxBytes=10240, backupCount=10)

    file_handler.setFormatter(
        logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s: %(lineno)d]'
        )
    )
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    with app.app_context():
        # Import parts of our application
        from core.blueprint import blueprint

        # Register Blueprints
        app.register_blueprint(blueprint, url_prefix="/api/v1")

        return app


cfg = DevelopmentConfig
if os.environ.get('FLASK_ENV') == 'production':
    cfg = ProductionConfig

app = create_app(cfg)
