from flask import Flask, session
from flask_login import LoginManager, UserMixin, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Y0uWillN3v3RGue55'
login_manager = LoginManager()
login_manager.init_app(app)

from app import views
from app import dbi
