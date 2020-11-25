import flask
from flask_login import login_required, current_user
from .models import Product, Cart
from . import shop_bp
from app.blueprints.authentication.models import User


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

@shop_bp.route("/cart")
@login_required
def show_cart():
    """Display the cart of the logged in user."""
    # Query all of the products the current user has in their cart
    users_cart_data = Cart.query.filter_by(user_id=current_user.id).all()
    products_full = [Product.query.get(cart_item.product_id) for cart_item in users_cart_data]

    # Consolidate the products array with a quantiy element
    products_count = {}
    products = []
    for product in products_full:
        if product in products_count:
            products_count[product] += 1
        else:
            products_count[product] = 1
    
    for product in products_count:
        products.append({
            "product": product, 
            "quantity": products_count[product]
            }
        )
    print(products)
    context = {
        "products": products
    }
    return flask.render_template("cart.html", **context)

@shop_bp.route("/cart/add/<int:product_id>")
@login_required
def add_to_cart(product_id):
    """Add the passed item to the cart as the current user."""
    # Get the id of the current user
    user_id = User.query.get(current_user.id).id

    # Combine user/product ids as a cart object
    data = {
        "user_id": user_id,
        "product_id": product_id
    }
    cart = Cart()
    cart.from_dict(data)
    cart.save()

    return flask.redirect(flask.request.referrer)
