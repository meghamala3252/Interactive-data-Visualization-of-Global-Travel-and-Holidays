import sys
import traceback
from project.app import create_app
from project.extensions import db

print("Attempting to create app...")
try:
    app = create_app()
    print("App created successfully.")
    
    print("Attempting to connect to DB...")
    with app.app_context():
        db.engine.connect()
        print("DB connected.")
        
except Exception as e:
    print("ERROR detected during startup:")
    print(e)
    traceback.print_exc()
