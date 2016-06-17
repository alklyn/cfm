from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
Bootstrap(app)

from app import views
from app import dbi
