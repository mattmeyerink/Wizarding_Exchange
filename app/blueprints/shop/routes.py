import flask
from . import shop_bp


@shop_bp.route("/")
def show_all_items():
    """Displays all of the items currently listed in the shop."""
    return flask.render_template("item_display.html")