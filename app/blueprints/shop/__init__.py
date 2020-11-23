import flask


shop_bp = flask.Blueprint("shop", __name__, url_prefix="/shop",
                          template_folder="shop_templates")

from . import routes, models
