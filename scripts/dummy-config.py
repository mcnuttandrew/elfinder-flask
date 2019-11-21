import os

DEBUG = False
TESTING = False
PORT = int(os.environ.get('PORT', '8000'))
HOST = os.environ.get('HOST', '127.0.0.1')
SECRET_KEY = os.urandom(24)
