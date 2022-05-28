# """Main file rendering all website pages."""
#
# import logging
# import random
# from collections import defaultdict
#
# from flask import flash, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required, login_user, logout_user
# from sqlalchemy import func
# from werkzeug.security import check_password_hash, generate_password_hash
#
# # from app import app, db, login_manager
# from application.db.game import AwayTeam, HomeTeam
# from application.db.names import spanish_f_names, spanish_l_names
# from application.db import Players
# from application.db.teams import Teams
# from application.db.users import Users
# from application.misc.oponents import teams_data
# from application.stadium import Stadium
# from application.weather.weather import Weather



@login_manager.user_loader
def load_user(user_id):
    """Flask-login user loader."""
    # Todo - place it somewhere else

    return Users.query.get(int(user_id))










if __name__ == "__main__":
    app.run(debug=True)
