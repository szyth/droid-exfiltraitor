from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False


app_config = {
    'development': Development,
    'production': Production,
}