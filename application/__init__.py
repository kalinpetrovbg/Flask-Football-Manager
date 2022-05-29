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
        from application.pages.main import main
        from application.pages.create_team import create_team
        from application.pages.multiplayer import multiplayer
        from application.pages.play_cup import play_cup
        from application.pages.quick_game import quick_game
        from application.misc.sample_db import create_sample
        from application.misc.update import update_teams

        app.register_blueprint(main)
        app.register_blueprint(create_team)
        app.register_blueprint(multiplayer)
        app.register_blueprint(play_cup)
        app.register_blueprint(quick_game)

        database = inspect(db.engine)

        if not database.has_table("fm_teams"):

            db.create_all()

            create_sample()
            update_teams()

        return app
