import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from exts import db
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login = LoginManager(app)
login.login_view = 'login'


if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


from app_name import routes, models, errors



