from flask import Flask

app = Flask(__name__)

from app import routes
from app.util import RandomGenerator, urlRepository