from flask import Flask
from flask_login import current_user
from project.config import Config
from project.extensions import db, migrate, login_manager, jwt, mail, socketio, cors, admin
from project.routes.auth import auth
from project.routes.main import main
from project.routes.api import api
from project.models import User, Dashboard, Insight, Badge, Timeline, Feedback
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/analytics_index.html')

class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role in ['Admin', 'Super Admin']

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    socketio.init_app(app)
    cors.init_app(app)
    # admin.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(api)

    # Admin Views
    # Note: In a production app with testing, you might want to ensure views aren't added twice.
    # For this setup, we'll add them here.
    # if len(admin._views) == 1: # Only 'Home' view exists by default
    #     admin.add_view(SecureModelView(User, db.session))
    #     admin.add_view(SecureModelView(Dashboard, db.session))
    #     admin.add_view(SecureModelView(Insight, db.session))
    #     admin.add_view(SecureModelView(Feedback, db.session))
    #     admin.add_view(SecureModelView(Timeline, db.session))
    #     admin.add_view(AnalyticsView(name='AI Analytics', endpoint='analytics'))

    # Flask-Login user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app

if __name__ == '__main__':
    app = create_app()
    socketio.run(app, debug=True)
