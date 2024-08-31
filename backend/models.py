from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bed_id = db.Column(db.Integer, db.ForeignKey('bed.id'), nullable=False)

class Bed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, default=True)
    patient = db.relationship('Patient', backref='bed', lazy=True)

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    symptoms = db.Column(db.String(255), nullable=False)
