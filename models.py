from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class VehicleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(150))
    contact = db.Column(db.Integer)
