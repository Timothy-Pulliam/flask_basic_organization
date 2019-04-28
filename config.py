import os

# Current Working Directory
pwd = os.getcwd()

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+pwd+'/databases/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS=False
SECRET_KEY = 'Thisisasecret!'
