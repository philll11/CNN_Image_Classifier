from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.jinja_env.filters['zip'] = zip

from app import routes
