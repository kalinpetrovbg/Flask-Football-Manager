from flask import Blueprint, render_template, redirect, request, flash, url_for, session
from flask_login import logout_user, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from application import db, login_manager
from application.models import Teams, Users

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    """Get user function."""
    return Users.get(user_id)


@auth.route("/login.html", methods=["GET", "POST"])
def login():
    """Renders Login page."""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = Users.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return render_template("login.html")

        login_user(user, remember=remember)
        return redirect("/profile.html")  # Todo

    elif request.method == "GET":
        return render_template("login.html")


@auth.route("/logout.html")
@login_required
def logout():
    """Renders Logout page."""

    logout_user()
    return redirect("/")


@auth.route("/signup.html", methods=["GET", "POST"])
def signup():
    """Renders Signup page."""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        existing_user = Users.query.filter_by(username=username).first()

        if existing_user:
            flash("There is already an user with this username.")
            return redirect("/signup.html")

        user = Users()
        user.username = username
        user.password = generate_password_hash(password, method="sha256")

        db.session.add(user)
        db.session.commit()

        return render_template("index.html")
    else:
        return render_template("signup.html")


@auth.route("/profile.html")
def profile():
    """Renders Profile page."""

    user = current_user
    if not current_user.is_authenticated:
        return redirect(url_for("nologin"))

    user_team = Teams.query.filter_by(id=user.team_id).first()

    try:
        opp_team = Teams.query.filter_by(id=session["opp_id"]).first()
    except KeyError:
        return render_template(
            "profile.html", user=user, user_team=user_team, opp_team=None
        )

    return render_template(
        "profile.html", user=user, user_team=user_team, opp_team=opp_team
    )


@auth.route("/no-login.html")
def nologin():
    """Error page for unauthorized users."""

    return render_template("no-login.html")
