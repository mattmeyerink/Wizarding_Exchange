import flask

main_bp = flask.Blueprint('main', __name__, url_prefix='',
                          template_folder='main_templates')

from . import routes
