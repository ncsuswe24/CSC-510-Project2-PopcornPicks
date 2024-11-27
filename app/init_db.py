"""
Module initializes SQAlchemy database
"""
from src import app, db
with app.app_context():
    db.create_all()
