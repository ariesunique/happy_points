from flask import Flask
from happy_points import api

def create_app(config_object="happy_points.settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    app.register_blueprint(api.routes.blueprint)
    return app


