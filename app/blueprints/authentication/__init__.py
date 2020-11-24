import flask


auth_bp = flask.Blueprint('authentication', __name__, url_prefix='/authentication',
                          template_folder='auth_templates')

from . import models, routes
