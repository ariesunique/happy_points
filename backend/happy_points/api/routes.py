from happy_points.api.models import Point
from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
import moment


blueprint = Blueprint("api", __name__)

PER_PAGE = 7


@blueprint.route("/")
def hello_world():
    return "Hello World!!"

@blueprint.route("/points")
def get_points():
    DATE_FORMAT = current_app.config["DATE_FORMAT"]
    page = int(request.args.get("page", 1))
    
    
    
    # query for a week's worth of data (ie, each page on the UI will show one week of data from Mon to Sat)
    # if user requested page 1, roll back to the previous Monday and show data within date range Mon to current
    # if user request page greater than 1, roll back the appropriate number of weeks
    
    # first get latest date in the database and rollback from that date (instead of rolling back from current date
    #      which could result in a lot of empty pages if data was not entered consistently for each day)
    
    latest_entry = Point.query.order_by(Point.timestamp.desc()).first()

    start_date = moment.date(latest_entry.timestamp).replace(weekday=1).subtract(week=page-1)
    end_date = start_date.clone().add(days=6)
    print(f"Start is {start_date.format('ddd MM-DD-YYYY')} and end is {end_date.format('ddd MM-DD-YYYY')}")
    

        
    
    points = [ point.to_dict() for point in Point.query.filter(Point.timestamp.between(start_date.date, end_date.date)).order_by(Point.timestamp.desc()).all() ]
    
    num_pages = len(points) // PER_PAGE
    if len(points) % PER_PAGE > 0: num_pages += 1 
    start = ( page - 1 ) * PER_PAGE
    end = start + PER_PAGE
    meta = {
        "num_pages": num_pages, 
        "prev_page": f"/points?page={page-1}" if page > 1 else "",
        "next_page": f"/points?page={page+1}" if page < num_pages else ""
    }
    return jsonify({"success": True,
                    "currentDate": moment.utcnow().format(DATE_FORMAT),
                    "totalEntries": len(points),
                    "numPages": num_pages,
                    "points": points,
                    "meta": meta
                   })

@blueprint.route("/points", methods=["POST"])
def add_points():
    return "add points"