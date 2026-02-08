from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from project.services.feedback_analyzer import analyze_feedback
from project.services.badges import check_and_award_badges
from project.ai_modules.insights import generate_insights_from_data
from project.ai_modules.story_mode import generate_story_script
from project.services.chatbot import get_chat_response
from project.models import Feedback, Insight, Timeline, Dashboard
from project.extensions import db
from datetime import datetime

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/generate_insight', methods=['POST'])
@login_required
def generate_insight():
    data = request.json
    dashboard_id = data.get('dashboard_id')
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    
    # Mocking OCR text data for now since we can't easily take a screenshot of the client-side iframe
    # In a real implementation with Puppeteer/Selenium, we'd grab the screenshot here.
    mock_text_data = "Tourist arrivals increased by 20% in 2023. France is top destination."
    
    insights_list = generate_insights_from_data(mock_text_data, {'title': dashboard.title})
    
    # Save insights to DB
    saved_insights = []
    for content in insights_list:
        new_insight = Insight(dashboard_id=dashboard.id, content=content, insight_type='Generated')
        db.session.add(new_insight)
        saved_insights.append({'content': content, 'date': datetime.utcnow().strftime('%Y-%m-%d')})
        
    # Log
    db.session.add(Timeline(user_id=current_user.id, action='Generated Insight', category='ai'))
    db.session.commit()
    
    # Check Badges
    check_and_award_badges(current_user.id, 'generate_insight')
    
    return jsonify({'message': 'Insights generated successfully!', 'insights': saved_insights, 'status': 'success'})

@api.route('/get_story', methods=['POST'])
@login_required
def get_story():
    data = request.json
    dashboard_id = data.get('dashboard_id')
    dashboard = Dashboard.query.get_or_404(dashboard_id)
    
    # Get existing insights to fuel the story
    insights = [i.content for i in dashboard.insights]
    if not insights:
        insights = ["Data shows stable trends.", "Visitor numbers are consistent."]
        
    script = generate_story_script({'title': dashboard.title}, insights)
    
    # Check Badges
    check_and_award_badges(current_user.id, 'story_mode')
    
    return jsonify({'script': script})

@api.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    response = get_chat_response(message)
    return jsonify({'response': response})

@api.route('/compare_dashboards', methods=['POST'])
@login_required
def compare_dashboards():
    # Logic to compare two dashboards
    return jsonify({'message': 'Comparison started'})

@api.route('/feedback', methods=['POST'])
@login_required
def submit_feedback():
    data = request.json
    content = data.get('content')
    dashboard_id = data.get('dashboard_id')
    
    category, sentiment = analyze_feedback(content)
    
    feedback = Feedback(
        user_id=current_user.id,
        dashboard_id=dashboard_id,
        content=content,
        category=category,
        sentiment=sentiment
    )
    db.session.add(feedback)
    db.session.commit()
    
    return jsonify({'message': 'Feedback received', 'category': category, 'reply': f"Thanks! We noted your {category.lower()}."})

