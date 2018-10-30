import os
# from postgres import DB_URI

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# For production use
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# For development use
# SQLALCHEMY_DATABASE_URI = 'postgres://nfxddaslfohcxn:430f8902fdb0.......'