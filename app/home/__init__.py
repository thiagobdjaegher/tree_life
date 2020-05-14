from flask import Blueprint

bl_home = Blueprint('bl_home', __name__, template_folder='templates', static_folder='static')

from . import views
