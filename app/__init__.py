import flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


# Creat instances of db and db migration
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Creates an instance of the Wizard Exchange Application."""
    # Initialize the flask app
    app = flask.Flask(__name__)

    # Add the configuration settings
    app.config.from_object(Config)

    # Link the db and db migration
    db.init_app(app)
    migrate.init_app(app, db)

    # Register the blueprints
    from .blueprints.main import main_bp
    app.register_blueprint(main_bp)

    from .blueprints.shop import shop_bp
    app.register_blueprint(shop_bp)

    # Create the db
    with app.app_context():
        db.create_all()

    return app
