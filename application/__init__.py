"""Create application and build database."""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from application.misc.sample_db import create_sample
        from application.misc.update import update_teams

        app.register_blueprint(routes.app_bp)

        database = inspect(db.engine)

        if not database.has_table("fm_teams"):

            db.create_all()

            create_sample()
            update_teams()

        return app
