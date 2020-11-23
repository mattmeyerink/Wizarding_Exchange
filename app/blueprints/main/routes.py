import flask
from . import main_bp


@main_bp.route("/")
def show_main():
    """Display the initial welcome page."""
    return flask.render_template("welcome_message.html")
