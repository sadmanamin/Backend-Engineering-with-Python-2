import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base configuration."""

    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:123456@db:5432/flask_project"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CACHE_TYPE = "redis"
    CACHE_REDIS_HOST = os.getenv('REDIS_SERVER', 'redis')
    CACHE_REDIS_POST = 6379
    CACHE_REDIS_DB = 0
    CACHE_REDIS_URL = "redis://"+CACHE_REDIS_HOST+":6379/0"
    CACHE_DEFAULT_TIMEOUT = 3300


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
