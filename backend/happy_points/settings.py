from environs import Env
import os

cwd = os.path.dirname(__file__)
basedir = os.path.abspath(cwd)

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = env.str("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = env.str("DATABASE_URL", default='sqlite:///' + os.path.join(basedir, 'happy.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATE_FORMAT = env.str("DATE_FORMAT", "ddd, MM-DD-YYYY")
