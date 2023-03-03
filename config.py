import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "app/static/images"

class DevConfig(Config):
    DEBUG = True
    UPLOAD_URL = "http://localhost:8080/static/images/"

class ProdConfig(Config):
    DEBUG = False
    UPLOAD_URL = "http://localhost:8080/static/images/"  # TODO: Change this
