import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()


######################################
#### Application Factory Function ####
######################################

def create_app(config_object_name='DevelopmentConfig'):
    app = Flask(__name__, instance_relative_config=True)
    app_settings = os.getenv(
    'APP_SETTINGS',
    'project.config.'+config_object_name
    )
    app.config.from_object(app_settings)
    return app
