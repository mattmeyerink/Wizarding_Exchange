import flask
from flask_login import login_required, current_user
from app import db
from .models import Product, Cart, get_user_cart_info
from . import shop_bp
from app.blueprints.authentication.models import User


@shop_bp.route("/")
def show_all_items():
    """Displays all of the items currently listed in the shop."""
    context = {
        "category": "All Products",
        "products": Product.query.all(),
        "cart_data": get_user_cart_info()
    }
    return flask.render_template("item_display.html", **context)

@shop_bp.route("/<category>")
def show_category(category):
    """Displays all of the items of a specific category."""
    context = {
        "category": category.title(),
        "products": Product.query.filter_by(category=category).all(),
        "cart_data": get_user_cart_info()
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
    total = 0
    for product in products_full:
        total += product.price
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

    context = {
        "products": products,
        "total": total,
        "cart_data": get_user_cart_info()
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

@shop_bp.route("/cart/delete/<int:product_id>")
@login_required
def delete_from_cart(product_id):
    """Delete a specific item from the user's cart."""
    # Get the id of the current user
    user_id = User.query.get(current_user.id).id 

    # Delete one instance of that product from the cart
    product_to_delete = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    db.session.delete(product_to_delete)
    db.session.commit()

    return flask.redirect(flask.url_for('shop.show_cart'))

@shop_bp.route("/cart/delete")
@login_required
def delete_cart():
    """Delete all of the items from user's cart."""
    # Get the id of the current user
    user_id = User.query.get(current_user.id).id 

    # Delete all of their products from the db
    products_to_delete = Cart.query.filter_by(user_id=user_id).all()
    for product in products_to_delete:
        db.session.delete(product)
    db.session.commit()

    return flask.redirect(flask.url_for('shop.show_cart'))


