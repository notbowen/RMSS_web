from flask import Flask

from config import DevConfig


def create_app(config_class=DevConfig):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register the blueprints
    from app.main import bp as frontend_bp
    app.register_blueprint(frontend_bp, url_prefix='/')

    from app.images import bp as images_bp
    app.register_blueprint(images_bp, url_prefix='/api/image')

    # Create a route for health checks
    @app.route('/health')
    def health():
        return 'OK'

    return app
