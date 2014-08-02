from app import db
from datetime import date


class Calls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    caller = db.Column(db.String(64))
    phone = db.Column(db.String(12))
    franchise = db.Column(db.String(64))
    location = db.Column(db.String(64))
    downtime = db.Column(db.Integer)
    plant_num = db.Column(db.Integer, nullable=True)
    machine = db.Column(db.String(64))
    tech = db.Column(db.String(64))
    problem = db.Column(db.String(128))
    comment = db.Column(db.String(128))

    def __repr__(self):
        return '<Calls %r>' % (self.machine)


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(5))
    name = db.Column(db.String(64))
