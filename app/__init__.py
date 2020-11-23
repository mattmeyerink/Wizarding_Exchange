import flask
from config import Config


def create_app():
    app = flask.Flask(__name__)
    app.config.from_object(Config)

    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    return app
