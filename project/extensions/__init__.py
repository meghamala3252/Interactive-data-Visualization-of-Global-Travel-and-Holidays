from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_cors import CORS

from flask_admin import Admin

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()
mail = Mail()
socketio = SocketIO(async_mode='threading')
cors = CORS()
admin = Admin(name='Global Tourism Admin')

login_manager.login_view = 'auth.login'
