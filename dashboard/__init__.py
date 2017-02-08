import os

# import logging
# from logging.handlers import RotatingFileHandler

from flask import Flask
from dashboard.mod_base.views import mod_base
from dashboard.mod_ec2.views import mod_ec2

buildmode = os.environ['APP_SETTINGS']

if buildmode is "production":
    buildmode = "config.ProductionConfig"
else:
    buildmode = "config.DevelopmentConfig"


app = Flask(__name__)
app.config.from_object(buildmode)
app.register_blueprint(mod_base)
app.register_blueprint(mod_ec2)
# app.logger.info("Loading configuraton from: " + buildmode)
print(" * Loading configuraton from: " + buildmode)
