from project.models import UserBadge, Badge, Timeline, User
from project.extensions import db
from datetime import datetime

def check_and_award_badges(user_id, action):
    """
    Checks if a user qualifies for a badge based on their actions.
    """
    user = User.query.get(user_id)
    if not user:
        return
    
    # Define Rules
    # 1. Explorer: View 5 different dashboards
    if action == 'view_dashboard':
        unique_views = Timeline.query.filter_by(user_id=user_id, category='view').count()
        if unique_views >= 5:
            award_badge(user, 'Explorer')

    # 2. Analyst: Generate 5 insights (Mock trigger)
    if action == 'generate_insight':
        insight_count = Timeline.query.filter_by(user_id=user_id, action='Generated Insight').count()
        if insight_count >= 5:
            award_badge(user, 'Analyst')

def award_badge(user, badge_name):
    badge = Badge.query.filter_by(name=badge_name).first()
    if badge:
        # Check if already owned
        if not UserBadge.query.filter_by(user_id=user.id, badge_id=badge.id).first():
            new_award = UserBadge(user_id=user.id, badge_id=badge.id)
            db.session.add(new_award)
            
            # Log event
            log = Timeline(user_id=user.id, action=f'Earned Badge: {badge_name}', category='badge')
            db.session.add(log)
            
            db.session.commit()
            print(f"Awarded {badge_name} to {user.username}")
