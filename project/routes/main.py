from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import func

from project.models import Badge, Dashboard, Timeline, UserBadge
from project.extensions import db
from project.ai_modules.itinerary import generate_itinerary
from project.ai_modules.recommend import get_recommendations
from project.services.badges import check_and_award_badges

main = Blueprint('main', __name__)

@main.route('/')
def index():
    public_dashboards = Dashboard.query.filter_by(is_public=True).limit(6).all()
    return render_template('index.html', dashboards=public_dashboards)

@main.route('/dashboard/<int:id>')
@login_required
def dashboard_view(id):
    dashboard = Dashboard.query.get_or_404(id)
    
    # Log to timeline (Synchronous but safe)
    timeline = Timeline(user_id=current_user.id, action='View Dashboard', category='view', metadata_json=f'{{"dashboard_id": {id}}}')
    db.session.add(timeline)
    db.session.commit()
    
    # Check Badges (Synchronous)
    check_and_award_badges(current_user.id, 'view_dashboard')
    
    # Get Recommendations (Optimized Query)
    recommendations = get_recommendations(current_user.id, id)
    
    return render_template('dashboard.html', dashboard=dashboard, recommendations=recommendations)

@main.route('/timeline')
@login_required
def timeline():
    events = current_user.timeline_events.order_by(Timeline.timestamp.desc()).all()
    return render_template('timeline.html', events=events)


@main.route('/profile')
@login_required
def profile():
    dashboard_count = current_user.dashboards.count()
    timeline_count = current_user.timeline_events.count()
    badge_count = current_user.badges.count()

    recent_dashboards = (
        current_user.dashboards.order_by(Dashboard.created_at.desc()).limit(4).all()
    )
    recent_activity = (
        current_user.timeline_events.order_by(Timeline.timestamp.desc()).limit(6).all()
    )

    badge_rows = (
        db.session.query(UserBadge, Badge)
        .join(Badge, UserBadge.badge_id == Badge.id)
        .filter(UserBadge.user_id == current_user.id)
        .order_by(UserBadge.awarded_at.desc())
        .all()
    )
    earned_badges = [
        {
            "name": badge.name,
            "description": badge.description,
            "icon_url": badge.icon_url,
            "awarded_at": link.awarded_at,
        }
        for link, badge in badge_rows
    ]

    category_rows = (
        db.session.query(Dashboard.category, func.count(Dashboard.id))
        .filter(Dashboard.user_id == current_user.id)
        .group_by(Dashboard.category)
        .order_by(func.count(Dashboard.id).desc())
        .limit(3)
        .all()
    )
    category_breakdown = [
        {"category": category or "Uncategorized", "count": count}
        for category, count in category_rows
    ]

    profile_progress = min(
        100,
        max(
            25,
            (dashboard_count * 12)
            + (badge_count * 18)
            + min(40, timeline_count // 2),
        ),
    )

    profile_stats = [
        {"label": "Dashboards Added", "value": dashboard_count, "tone": "primary"},
        {"label": "Badges Earned", "value": badge_count, "tone": "accent"},
        {"label": "Activity Events", "value": timeline_count, "tone": "muted"},
    ]

    return render_template(
        "profile.html",
        profile_stats=profile_stats,
        recent_dashboards=recent_dashboards,
        recent_activity=recent_activity,
        earned_badges=earned_badges,
        category_breakdown=category_breakdown,
        profile_progress=profile_progress,
    )

@main.route('/itinerary', methods=['GET', 'POST'])
@login_required
def itinerary():
    result = None
    if request.method == 'POST':
        destination = request.form.get('destination')
        month = request.form.get('month')
        days = request.form.get('days')
        budget = request.form.get('budget')
        
        result = generate_itinerary(destination, days, budget, month)
        
        # Log
        db.session.add(Timeline(user_id=current_user.id, action=f'Planned Trip to {destination}', category='itinerary'))
        db.session.commit()
        
    return render_template('itinerary.html', result=result)

@main.route('/compare')
@login_required
def compare():
    dashboards = Dashboard.query.all()
    return render_template('compare.html', dashboards=dashboards)

@main.route('/add_dashboard', methods=['GET', 'POST'])
@login_required
def add_dashboard():
    if request.method == 'POST':
        title = request.form.get('title')
        embed_url = request.form.get('embed_url')
        country = request.form.get('country')
        category = request.form.get('category')
        tags = request.form.get('tags')
        
        new_dashboard = Dashboard(
            title=title,
            embed_url=embed_url,
            country=country,
            category=category,
            tags=tags,
            creator=current_user,
            is_public=True
        )
        db.session.add(new_dashboard)
        db.session.commit()
        
        flash('Dashboard added successfully!', 'success')
        return redirect(url_for('main.index'))
        
    return render_template('add_dashboard.html')

