import os
import tempfile
import datetime as dt
import moment
import random

import pytest
from webtest import TestApp as T

from happy_points.app import create_app
from happy_points.api.models import Point
from happy_points import db as _db
from .factories import PointFactory

from factory import Sequence, LazyFunction
from factory.alchemy import SQLAlchemyModelFactory


@pytest.fixture
def app():
    _app = create_app("tests.settings")
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()
    
    
@pytest.fixture 
def client(app):
    return T(app)


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()
        
    yield _db
    
    _db.session.close()
    _db.drop_all()
    

    

# ----- API Tests ------ #
    
    
@pytest.mark.api    
def test_get_points_empty_db(client, db):
    """Get all the points via the api"""
    resp = client.get("/points")
    assert resp.status_code == 200
    payload = resp.json
    assert payload.get("success")
    assert payload.get("points") != None
   
    points = payload.get("points")
    assert len(points) == 0
    
    
@pytest.mark.api  
def test_get_points(client, db):
    """Get all the points via the api"""
    # first add data points to the db so there is something to retrieve
    successfully_added_data = (point.save() for point in PointFactory.create_batch(size=5))    
    
    resp = client.get("/points")
    assert resp.status_code == 200
    payload = resp.json
    assert payload.get("success")
    assert payload.get("points") != None
   
    points = payload.get("points")
    assert len(points) == 5
    
    
@pytest.mark.api       
def test_create_point(client, db):
    """Create a new entry via the api"""
    HAPPY = 100
    SAD = 20
    MSG = "Very good"
    params = {"happy": HAPPY, "sad": SAD, "notes": MSG }   
    resp = client.post_json("/points", params=params)
    assert resp.status_code == 200
    
    # verify that the response contains the data that we sent
    payload = resp.json
    assert payload.get("success")
    assert payload.get("point") != None    
    assert payload.get("point").get("numHappy") == HAPPY
    assert MSG in payload.get("point").get("notes")
    
    # verify that the new point is actually in the database
    retrieved = Point.query.get(payload.get("point").get("id"))
    assert retrieved 
    assert retrieved.happy == HAPPY
    assert retrieved.sad == SAD
    assert retrieved.total == HAPPY - SAD
    assert MSG in retrieved.notes
                   
        
@pytest.mark.api   
def test_update_with_some_parameters(client):
    pass
    

@pytest.mark.api       
def test_update_point(client, db):
    # first add data points to the db so there is something to retrieve;
    # point is added with a default current timestamp
    point = Point(happy=5)
    point.save()
    
    # use the api to update the entry with a timestamp from today
    HAPPY = 95
    params = {"happy": HAPPY }   
    resp = client.post_json("/points", params=params)
    
    # check that our point now has 100 happy faces
    assert point.happy == 100


@pytest.mark.api
def test_api_error(client, db):
    pass


@pytest.mark.api
def test_paging(client, db):
    # add 8 days worth of data from Sun Apr 19, 2020 - Sun Apr 26, 2020
    # get current date and set to prev Sun (week starts on Monday)
    # this way, with 8 days of data, we will get a full week on one page, 
    #    and one overflow date on page 2
    sunday = moment.date(2020, 4, 26)
    for i in range (8):
        prev = sunday.clone().subtract(days=i)
        point = Point(happy=5)
        point.timestamp = prev.date
        point.save()
        
    assert len(Point.query.all()) == 8, "Data loaded incorrectly"
    
    # get first page of data
    resp = client.get("/points")
    print(resp)
    assert resp.status_code == 200
    assert resp.json.get("success")
    assert resp.json.get("points") != None
    assert resp.json.get("meta").get("next_page")
   
    points = resp.json.get("points")
    assert len(points) == 7
    
    # get the next page of data
    resp = client.get("/points?page=2")
    assert len(resp.json.get("points")) == 1
    assert "04-19-2020" in resp.json.get("points")[0].get("date")
    

@pytest.mark.api
def test_paging_nonconsecutive_dates(client, db):
    pass


@pytest.mark.api
def test_paging_old_weekold_entries(client, db):
    pass




def test_factory(db):
    point = PointFactory()
    assert point 
    
    
def test_batch_factories(db):
    points = []
    for i in range(4):
        points.append(PointFactory())
    assert len(points) == 4

                  
    
# ----- DB Tests ------ #

@pytest.mark.db
def test_create_point_with_db_defaults(db):
    """Ensure that a new Point entry in the database has the correct default values"""
    point = Point()
    point.save()
    assert point.id, "the object should have an id if successfully saved in the db"
    
    retrieved = Point.query.get(point.id)
    assert retrieved == point, "the database object returned should be the same as the one just created"
    
    assert bool(point.timestamp)
    assert isinstance(point.timestamp, dt.datetime)
    assert point.happy == 0, "happy column should be initialized to 0"
    assert point.sad == 0, "sad column should be initialized to 0"
    assert point.total == 0, "total column should be initialized to 0"
    

@pytest.mark.db
def test_create_point_with_automatic_total(db):
    """Ensure that the total column is correctly set to the difference between happy and sad"""
    point = Point(happy=5, sad=3)
    point.save()
    assert point.total == 2, "total column should be set to the value of happy - sad"
    

@pytest.mark.db
def test_total_is_not_created_negative(db):
    """Ensure that the total column is never a negative number, even if there are more sad faces than happy"""
    point = Point(happy=1, sad=5)
    point.save()
    assert point.total == 0, "total column should never be negative"
    

@pytest.mark.db
def test_update_point(db):
    """Ensure that we can update a database entry"""
    point = Point()
    point.save()
    
    point.happy = 5
    point.sad = 3
    point.save()
    
    assert point.id, "the object should have an id if successfully saved in the db"
    
    retrieved = Point.query.get(point.id)
    assert retrieved.happy == 5
    assert retrieved.sad == 3
    assert retrieved.total == 2, "the total column should automatically be set to happy-sad"
    

    