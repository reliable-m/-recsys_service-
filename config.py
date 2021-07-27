class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = "./static/uploads"


class ProductionConfig(Config):
    UPLOAD_FOLDER = "./static/uploads"


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_FOLDER = "./static/uploads"


class TestingConfig(Config):
    TESTING = True
    UPLOAD_FOLDER = "./static/uploads"
