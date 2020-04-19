from flask import Flask
from happy_points import api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from . import db, migrate

def create_app(config_object="happy_points.settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)

    # register extensions
    db.init_app(app)
    migrate.init_app(app, db)    
    
    # register api blueprint
    app.register_blueprint(api.routes.blueprint)
    
    
    return app


