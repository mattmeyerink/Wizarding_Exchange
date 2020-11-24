"""Define models necissary for the shop functionality."""
import flask
from datetime import datetime
from app import db


class Product(db.Model):
    """Table in db to store data for the products."""
    __tablename__ = "products"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text())
    price = db.Column(db.Float())
    category = db.Column(db.String())
    image = db.Column(db.String())
    tax = db.Column(db.Float())
    description = db.Column(db.Text())
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def save(self):
        """Add the product to the db."""
        db.session.add(self)
        db.session.commit()

    def remove(self):
        """Remove the product from the db."""
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f"<Product: {self.name}=>{self.price}>"

    def from_dict(self, data):
        """Assigns variables for product based on input dict."""
        for field in ["name", "price", "category", "image", "tax", "description"]:
            if field in data: 
                setattr(self, field, data[field])

    def to_dict(self):
        """Returns the products characteristics as a dict."""
        data = {
            "id": self.id,
            "name": self.name, 
            "price": self.price,
            "image": self.image,
            "category": self.category,
            "tax": self.tax,
            "description": self.description
        }
        return data
        