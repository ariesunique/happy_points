from happy_points.api.models import Point
from flask import Blueprint, jsonify

blueprint = Blueprint("api", __name__)

@blueprint.route("/")
def hello_world():
    return "Hello World!!"

@blueprint.route("/points")
def get_points():
    points = [ point.to_dict() for point in Point.query.all() ]
    print(points)
    return jsonify({"success": True,
                    "points": points
                   })

@blueprint.route("/points", methods=["POST"])
def add_points():
    return "add points"