from project.extensions import db
from datetime import datetime

class Dashboard(db.Model):
    __tablename__ = 'dashboards'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    embed_url = db.Column(db.String(512)) # Power BI Embed URL
    country = db.Column(db.String(64))
    category = db.Column(db.String(64))
    tags = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_public = db.Column(db.Boolean, default=True)
    
    insights = db.relationship('Insight', backref='dashboard', lazy='dynamic')
    feedbacks = db.relationship('Feedback', backref='dashboard', lazy='dynamic')

class Insight(db.Model):
    __tablename__ = 'insights'
    
    id = db.Column(db.Integer, primary_key=True)
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboards.id'))
    content = db.Column(db.Text)
    insight_type = db.Column(db.String(50)) # Generated, Story, Comparison
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Badge(db.Model):
    __tablename__ = 'badges'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256))
    icon_url = db.Column(db.String(256))

class Timeline(db.Model):
    __tablename__ = 'timeline'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    action = db.Column(db.String(128)) # View Dashboard, Earned Badge, etc.
    category = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    metadata_json = db.Column(db.Text) # Store extra details like dashboard_id in JSON

class Feedback(db.Model):
    __tablename__ = 'feedback'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboards.id'), nullable=True)
    content = db.Column(db.Text)
    category = db.Column(db.String(50)) # Bug, Feature, etc. (AI Classified)
    sentiment = db.Column(db.String(20)) # Positive, Negative, Neutral
    status = db.Column(db.String(20), default='New')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
