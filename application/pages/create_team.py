from flask import Blueprint, render_template
from flask_login import current_user

from application.models import Teams

create_team = Blueprint("create_team", __name__)



