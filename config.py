import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__name__))
load_dotenv(os.path.join(basedir, ".env"))

class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")

    SECRET_KEY = os.getenv("SECRET_KEY")

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    STRIPE_SK_TEST = os.getenv('STRIPE_SK_TEST')
    STRIPE_PK_TEST = os.getenv('STRIPE_PK_TEST')
    STRIPE_SUCCESS_URL = os.getenv('STRIPE_SUCCESS_URL')
    STRIPE_CANCEL_URL = os.getenv('STRIPE_CANCEL_URL')
    