from happy_points import db
from datetime import datetime

class Point(db.Model):
    __tablename__ = "point"
    id = db.Column(db.Integer, primary_key=True)
    happy = db.Column(db.Integer, default=0)
    sad = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    notes = db.Column(db.String(300))
    
    def __repr__(self):
        return f"<Point({self.id}) added {self.timetamp}>"