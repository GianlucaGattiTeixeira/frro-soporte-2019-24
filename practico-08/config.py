import os

UPLOAD_FOLDER = os.path.abspath("./uploads/")
DBURI = "mysql://{username}:{password}@{hostname}/{database}".format(
    username='soporte2019',
    password='soporte2019',
    hostname = 'localhost:3306',
    database = 'vinos_mercado_libre_bebidas'
)

class Config(object):
    DEBUG = False
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = UPLOAD_FOLDER

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DBURI
    SECRET_KEY = os.urandom(16)

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DBURI