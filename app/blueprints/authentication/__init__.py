import flask


auth_bp = flask.Blueprint('auth', __name__, url_prefix='/authentication',
                          template_folder='auth_templates')

from . import models, routes
