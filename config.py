class BaseConfig (object):
    DEBUG = False
    SECRET_KEY = 'duaracoin'

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    DEBUG = False