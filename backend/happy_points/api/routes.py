from happy_points import app
from flask import Blueprint

blueprint = Blueprint("api", __name__)

@blueprint.route("/")
def hello_world():
    return "Hello World!!"

@blueprint.route("/points")
def get_points():
    pass

@blueprint.route("/points", method="POST")
def add_points():
    pass