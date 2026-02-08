import os
from project.app import create_app
from project.extensions import db
from project.models import User, Dashboard, Badge, Timeline

app = create_app()

def seed_data():
    with app.app_context():
        print("Seeding database...")
        
        # Create Admin User
        if not User.query.filter_by(email='admin@example.com').first():
            admin = User(username='admin', email='admin@example.com', role='Admin', is_verified=True)
            admin.set_password('admin123')
            db.session.add(admin)
            print("Created Admin User (email: admin@example.com, pass: admin123)")

        # Create Standard User
        if not User.query.filter_by(email='user@example.com').first():
            user = User(username='demo_user', email='user@example.com', role='User', is_verified=True)
            user.set_password('user123')
            db.session.add(user)
            print("Created Demo User (email: user@example.com, pass: user123)")

        # Create Badges
        badges = [
            {'name': 'Explorer', 'description': 'Visited 5 different dashboards', 'icon_url': 'explorer.png'},
            {'name': 'Analyst', 'description': 'Generated 10 AI insights', 'icon_url': 'analyst.png'},
            {'name': 'Story Master', 'description': 'Completed 3 story modes', 'icon_url': 'story.png'},
            {'name': 'Trend Hunter', 'description': 'Compared 5 destinations', 'icon_url': 'trend.png'}
        ]
        
        for b in badges:
            if not Badge.query.filter_by(name=b['name']).first():
                new_badge = Badge(name=b['name'], description=b['description'], icon_url=b['icon_url'])
                db.session.add(new_badge)
        
        print("Created Badges")

        # Create Sample Dashboard
        # Note: This is a public Microsoft Power BI Demo URL for testing purposes
        sample_url = "https://app.powerbi.com/view?r=eyJrIjoiODZhOTViZWItNTUwMy00OGFkLWEwYjItYTE0ODc0Y2ExYjhlIiwidCI6IjI4ZTIyNWY5LWE4NTEtNDViMy05MTcxLTAxY2M1NWNiYTYxNiIsImMiOjZ9"
        
        if not Dashboard.query.filter_by(title='Global Tourism Overview').first():
            # Assign to admin
            admin_user = User.query.filter_by(email='admin@example.com').first()
            
            dash = Dashboard(
                title='Global Tourism Overview',
                embed_url=sample_url,
                country='Global',
                category='General',
                tags='tourism,global,trends',
                creator=admin_user,
                is_public=True
            )
            db.session.add(dash)
            print("Created Sample Dashboard")

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
