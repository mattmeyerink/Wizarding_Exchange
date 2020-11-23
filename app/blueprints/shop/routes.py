import flask
from .models import Product
from . import shop_bp


@shop_bp.route("/")
def show_all_items():
    """Displays all of the items currently listed in the shop."""
    context = {
        "category": "All Products",
        "products": Product.query.all()
    }
    return flask.render_template("item_display.html", **context)

@shop_bp.route("/<category>")
def show_category(category):
    """Displays all of the items of a specific category."""
    context = {
        "category": category.title(),
        "products": Product.query.filter_by(category=category).all()
    }
    return flask.render_template("item_display.html", **context)
