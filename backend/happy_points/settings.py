from environs import Env
import os
basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL", default='sqlite:///' + os.path.join(basedir, 'happy.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False