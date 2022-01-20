import os

POSTGRES_SERVER_NAME = os.environ.get('POSTGRES_SERVER_NAME','36.255.69.121')
POSTGRES_USER_NAME = os.environ.get('POSTGRES_USER_NAME','postgres')

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://' + POSTGRES_USER_NAME +':123456@' + POSTGRES_SERVER_NAME + ':5432/'
database_name = 'flask'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    SECURITY_PASSWORD_SALT = 'my_precious_two'
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    # MAIL_USE_TLS = False
    # MAIL_USERNAME = 'email@example.com'
    # MAIL_PASSWORD = 'password'
    # MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
