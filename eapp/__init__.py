from flask import Flask
from eapp.model import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '989186ng39ks23akvnjkf342u923alnf3'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///eapp.sqlite3"


db.init_app(app)
ALLOWED_EXTENSIONS = set(['jpeg', 'jpg', 'png'])
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.app_context().push()
from eapp import routes
