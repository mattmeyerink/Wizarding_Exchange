"""Define models necissary for the shop functionality."""
import flask
from datetime import datetime
from app import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Float())
    image = db.Column(db.String())
    tax = db.Column(db.Float())
    description = db.Column(db.Text())
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
