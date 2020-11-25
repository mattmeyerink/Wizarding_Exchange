import flask
from . import auth_bp
from .models import User
from flask_login import login_user, logout_user, current_user
from .forms import RegistrationForm

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    """Handle loging into the site."""
    # Check if login info was submitted
    if flask.request.method == "POST":
        # Retrieve the form data from post request
        form_data = flask.request.form.to_dict()
        email = form_data.get("email")
        password = form_data.get("password")

        # Attempt to pull users information from the db
        user = User.query.filter_by(email=email).first()

        # Check if the user in db and password input is correct
        if user and user.check_password_hash(password):
            # Login the user and route them back to the main product page
            login_user(user)
            return flask.redirect(flask.url_for("shop.show_all_items"))
        
        flask.flash("Invalid login credentials", "warning")
        return flask.redirect(flask.url_for("authentication.login"))

    return flask.render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    """Registers a new user to the db."""
    form = RegistrationForm()

    # Check if the form object passed was submitted correctly
    if form.validate_on_submit():
        # Gather data from the form submit
        data = {
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": form.email.data
        }
        password = form.password.data
        # Attempt to add a new user to the db with the form data and route to login
        try:
            user = User()
            user.from_dict(data)
            user.hash_passowrd(password)
            user.save()
            return flask.redirect(flask.url_for("authentication.login"))

        # Flash an error message and reroute to registration on error
        except Exception as error:
            flask.flash("Error while registering", "warning")
            return flask.redirect(flask.url_for("authentication.register"))
    context = {
        "form": form
    }
    return flask.render_template("register.html", **context)

@auth_bp.route("/logout")
def logout():
    """logout the current user."""
    logout_user()
    return flask.redirect(flask.url_for("authentication.login"))
