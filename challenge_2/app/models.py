

from app import db

Base = db.Model

class Details(Base):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email_address = db.Column(db.String(), unique=True)
    date_registered = db.Column(db.DateTime)

