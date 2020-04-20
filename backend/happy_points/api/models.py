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
    
    
    def __init__(self, happy=0, sad=0, notes=""):
        self.happy = happy
        self.sad = sad
        self.notes = notes
        self.set_total()
        
    
    def set_total(self):
        self.total = self.happy - self.sad if self.happy > self.sad else 0
    
    def __repr__(self):
        return f"<Point({self.id}) added {self.timestamp}; happy: {self.happy}; sad: {self.sad}; total: {self.total}; notes: {self.notes}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "numHappy": self.happy,
            "numSad": self.sad,
            "totalPoints": self.total,
            "date": self.timestamp,
            "notes": self.notes
               }
    
    
    def save(self, commit=True):
        self.set_total()
        db.session.add(self)
        return commit and db.session.commit()
        