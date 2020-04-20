import os
import tempfile
import datetime as dt
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

def test_hello_world(client):
    rv = client.get("/")
    print(rv)
    assert rv.status_code == 200
    assert 'Hello World' in rv.text
    
    
def test_get_points(client, db):
    """Get all the points via the api"""
    resp = client.get("/points")
    assert resp.status_code == 200
    payload = resp.json
    assert payload.get("success")
    assert payload.get("points") != None
   
    points = payload.get("points")
    print(resp)
    assert len(points) == 3
    

def test_factory(db):
    point = PointFactory()
    assert point 
    
    
def test_batch_factories(db):
    points = []
    for i in range(4):
        points.append(PointFactory())
    assert len(points) == 4

                  
    
# ----- DB Tests ------ #

def test_create_point_with_db_defaults(db):
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
    
    
def test_create_point_with_automatic_total(db):
    point = Point(happy=5, sad=3)
    point.save()
    assert point.total == 2, "total column should be set to the value of happy - sad"
    
    
def test_total_is_not_created_negative(db):
    point = Point(happy=1, sad=5)
    point.save()
    assert point.total == 0, "total column should never be negative"
    
    
def test_update_point(db):
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
    

    