from project.models import Dashboard

def get_recommendations(user_id, current_dashboard_id=None):
    """
    Mock Content-Based Filtering Recommendation Engine.
    """
    # In a real app, this would use Sentence-BERT on tags/categories
    
    # Return up to 3 recommendations
    recommendations = Dashboard.query.filter(Dashboard.id != current_dashboard_id).limit(3).all()
    
    return recommendations
