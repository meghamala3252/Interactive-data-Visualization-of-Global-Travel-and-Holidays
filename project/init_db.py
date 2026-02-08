from project.app import create_app
from project.extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created.")
