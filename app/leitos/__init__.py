from flask import Blueprint

bl_leitos = Blueprint('bl_leitos', __name__, template_folder='templates', static_folder='static')

from . import views
