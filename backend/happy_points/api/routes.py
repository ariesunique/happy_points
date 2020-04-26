from happy_points.api.models import Point
from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
import moment


blueprint = Blueprint("api", __name__)

@blueprint.route("/")
def hello_world():
    return "Hello World!!"

@blueprint.route("/points")
def get_points():
    DATE_FORMAT = current_app.config["DATE_FORMAT"]
    page = int(request.args.get("page", 1))    
    points = []    
    total = 0
    # query for a week's worth of data (ie, each page on the UI will show one week of data from Mon to Sat)
    # if user requested page 1, roll back to the previous Monday and show data within date range Mon to current
    # if user request page greater than 1, roll back the appropriate number of weeks
    
    # first get latest date in the database and rollback from that date (instead of rolling back from current date
    #      which could result in a lot of empty pages if data was not entered consistently for each day)
    
    
    latest_entry = Point.query.order_by(Point.timestamp.desc()).first()
    earliest_entry = Point.query.order_by(Point.timestamp.asc()).first()

    if latest_entry:
        start_date = moment.date(latest_entry.timestamp).replace(weekday=1).subtract(week=page-1)
        end_date = start_date.clone().add(days=6)

        points_from_db = Point.query.filter(Point.timestamp.between(start_date.date, end_date.date)).order_by(Point.timestamp.desc()).all()
        points = [ point.to_dict() for point in points_from_db ]
        total = sum( point.total for point in points_from_db )
        
    meta = {
        "current_page": request.url , 
        "prev_page": "/points?page={page-1}" if page > 1 else "",
        "next_page": "/points?page={page+1}" if earliest_entry and start_date and earliest_entry.timestamp < start_date.date else ""
    }
    return jsonify({"success": True,
                    "currentDate": moment.now().format(DATE_FORMAT),
                    "totalPoints": total,
                    "points": points,
                    "meta": meta
                   })

@blueprint.route("/points", methods=["POST"])
def add_points():

    happy_val = request.get_json().get("happy", 0)
    sad_val = request.get_json().get("sad", 0)
    notes_val = request.get_json().get("notes", "")    
    
    # get the entry for the current date and update it
    start = moment.now().zero.date
    end = moment.now().replace(hours=23, minutes=59, seconds=59).date
    todays_point = Point.query.filter(Point.timestamp.between(start, end)).first()
    
    if todays_point:
        todays_point.happy += happy_val
        todays_point.sad += sad_val
        todays_point.notes += ";" + notes_val
    else:
        todays_point = Point(happy_val, sad_val, notes_val)
        
    todays_point.save()
    

    return jsonify({"success": True,
                    "point": todays_point.to_dict()
                   })