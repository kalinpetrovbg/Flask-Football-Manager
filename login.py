from flask_login import LoginManager
from fm.app import app


login_manager = LoginManager()
login_manager.init_app(app)