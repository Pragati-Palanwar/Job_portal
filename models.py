from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobSeeker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    availability = db.Column(db.Text, nullable=False)
    other_details = db.Column(db.Text, nullable=False)

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    company_name = db.Column(db.Text, nullable=False)
    job_requirements = db.Column(db.Text, nullable=False)
    contact_details = db.Column(db.Text, nullable=False)
