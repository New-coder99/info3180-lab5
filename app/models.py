# Add any model classes for Flask-SQLAlchemy here
from datetime import datetime
from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.description}', '{self.poster}', '{self.created_at}')"
    def __init__(self, title, description, poster):
        self.title = title
        self.description = description
        self.poster = poster
