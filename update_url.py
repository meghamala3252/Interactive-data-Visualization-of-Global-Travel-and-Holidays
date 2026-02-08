from project.app import create_app
from project.extensions import db
from project.models import Dashboard

app = create_app()

def update_url():
    print("Please paste your full Power BI Embed URL below and press Enter:")
    new_url = input().strip()
    
    if not new_url:
        print("No URL provided. Exiting.")
        return

    with app.app_context():
        dash = Dashboard.query.filter_by(title='Global Tourism Overview').first()
        if dash:
            dash.embed_url = new_url
            db.session.commit()
            print("---------------------------------------------------")
            print("✅ Dashboard URL updated successfully!")
            print(f"New URL: {new_url}")
            print("---------------------------------------------------")
        else:
            print("❌ Error: Dashboard 'Global Tourism Overview' not found in database.")

if __name__ == '__main__':
    update_url()
