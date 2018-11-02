import os
# from postgres import DB_URI

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

# For production use
#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

# For development use
#SQLALCHEMY_DATABASE_URI = 'postgres://nfxddaslfohcxn:430f8902fdb00d28c1a122b61a73761aaf2d6eaa87103d7c3e5400b9994c128b@ec2-54-243-46-32.compute-1.amazonaws.com:5432/d2r4bdi1dne77i'
CRUD_DATABASE_URI = 'postgres://nfxddaslfohcxn:430f8902fdb00d28c1a122b61a73761aaf2d6eaa87103d7c3e5400b9994c128b@ec2-54-243-46-32.compute-1.amazonaws.com:5432/d2r4bdi1dne77i'

COMPONENT_DATABASE_URI = 'postgres://wovnsfhsncbkic:3deced8a979dff8d76e6c55228870dea216b57532a070c1a4cf6a9d984bce0e3@ec2-54-243-46-32.compute-1.amazonaws.com:5432/d882452k9qqs4f'

RECOMMEND_DATABASE_URI = 'postgres://gkedxhsabubkjq:f8686d5d199ffa209ab2d8aa265f5aec20f19f10d26ce5f20efd2bd9963ce23a@ec2-174-129-236-147.compute-1.amazonaws.com:5432/d8dj0rc7e9duhi'