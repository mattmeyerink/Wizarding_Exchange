from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """Class to represent a user of the site."""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, index=True)
    password = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User: {self.id} | {self.email}>"

    def save(self):
        """Commit the user's information to the db."""
        db.session.add(self)
        db.session.commit()

    def hash_passowrd(self, original_password):
        """Hash the input password to store in the db."""
        self.password = generate_password_hash(original_password)

    def check_password_hash(self, original_password):
        """Compare the input password to the hased password in db."""
        return check_password_hash(self.password, original_password)
    
    def from_dict(self, data):
        """Create a new user from a dictionary of user info."""
        for field in ["first_name", "last_name", "email"]:
            if field in data:
                setattr(self, field, data[field])
        
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
