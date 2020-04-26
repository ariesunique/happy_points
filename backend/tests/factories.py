import random

from happy_points.api.models import Point
from happy_points import db as _db

from factory import Sequence, LazyFunction
from factory.alchemy import SQLAlchemyModelFactory

common_notes = ["listening the first time",
               "being rude",
                "excellent work",
                "helping clean up",
                "talking back",
                "playing nicely with others"
               ]

class PointFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = _db.session
        sqlalchemy_session_persistence = "commit"
        model = Point
        
    happy = random.randint(1, 3)
    sad = random.randint(1,3)
    notes = []
    for _ in range(random.randint(0,2)):
        notes.append(random.choice(common_notes))
    notes = ";".join(notes)
        
    