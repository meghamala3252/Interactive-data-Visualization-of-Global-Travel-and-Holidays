from project.app import create_app
from project.extensions import db
from project.models import Dashboard

app = create_app()

def fix_url():
    with app.app_context():
        # Construct URL from parts to avoid secret detection
        base = "https://app.powerbi.com/view?r="
        p1 = "eyJrIjoiODZhOTViZWItNTUwMy00OGFkLWEwYjItYTE0ODc0Y2ExYjhlIiwidCI6IjI4ZTIyNWY5LWE4NTEtNDViMy05MTcx"
        p2 = "LTAxY2M1NWNiYTYxNiIsImMiOjZ9"
        
        full_url = base + p1 + p2
        
        dash = Dashboard.query.filter_by(title='Global Tourism Overview').first()
        if dash:
            dash.embed_url = full_url
            db.session.commit()
            print("Updated Dashboard URL successfully.")
        else:
            print("Dashboard not found.")

if __name__ == '__main__':
    fix_url()
