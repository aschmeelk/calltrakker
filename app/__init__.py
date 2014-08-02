from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_object('config')
app.config.update(
    SECRET_KEY='youllneverguess'
)
db = SQLAlchemy(app)

from app import views, models



