from happy_points.api.models import Point
from flask import Blueprint

blueprint = Blueprint("api", __name__)

@blueprint.route("/")
def hello_world():
    return "Hello World!!"

@blueprint.route("/points")
def get_points():
    return "get  points"

@blueprint.route("/points", methods=["POST"])
def add_points():
    return "add points"