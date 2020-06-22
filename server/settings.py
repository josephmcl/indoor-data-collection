import os
from environs import Env

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


env = Env()
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SECRET_KEY = env.str('SECRET_KEY', default='super-secret')
SECURITY_PASSWORD_HASH = 'HASH'
SECURITY_PASSWORD_SALT = 'SALT'

#  Sqlalchemy Settings
SQLALCHEMY_DATABASE_URI = env.str(
    'DATABASE_URI',
    default='sqlite:///' + os.path.join(ROOT_DIR, 'app.db')
)
SQLALCHEMY_TRACK_MODIFICATIONS = ENV == 'development'
#  Praetorian Auth Token Settings
JWT_ACCESS_LIFESPAN = {'hours': 24}
JWT_REFRESH_LIFESPAN = {'days': 30}
