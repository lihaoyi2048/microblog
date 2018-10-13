import os

DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo5'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(DIALECT, DRIVER, USERNAME,
                                                                              PASSWORD, HOST, PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 3
