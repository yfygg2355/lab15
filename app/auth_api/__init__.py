from flask import Blueprint

auth_api_bp = Blueprint('auth_api', __name__, url_prefix='/api/auth')

from . import views