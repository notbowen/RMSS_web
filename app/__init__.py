from flask import Flask

from config import DevConfig
from app.extensions import db


def create_app(config_class=DevConfig):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialise database
    db.init_app(app)

    # Register the blueprints
    from app.main import bp as frontend_bp
    app.register_blueprint(frontend_bp, url_prefix='/')

    from app.images import bp as images_bp
    app.register_blueprint(images_bp, url_prefix='/api/image')

    from app.questions_backend import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/api/question')

    from app.questions_frontend import bp as questions_frontend_bp
    app.register_blueprint(questions_frontend_bp, url_prefix='/questions')

    from app.topics import bp as topics_bp
    app.register_blueprint(topics_bp, url_prefix='/topics')

    # Create a route for health checks
    @app.route('/health')
    def health():
        return 'OK'

    return app
