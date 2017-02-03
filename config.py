import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = "0.0.0.0"
    PORT = 8085
    SECRET_KEY = "beevadev"
    ENCRYPTION_ALGORITHM = 'HS256'
    DEBUG = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'auth.db')
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
