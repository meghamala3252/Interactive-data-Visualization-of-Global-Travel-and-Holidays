from project.app import create_app
from project.extensions import db
from project.models import Dashboard

app = create_app()

def check_url():
    with app.app_context():
        dash = Dashboard.query.filter_by(title='Global Tourism Overview').first()
        if dash:
            print(f"Current URL in DB: {dash.embed_url}")
        else:
            print("Dashboard not found.")

if __name__ == '__main__':
    check_url()
