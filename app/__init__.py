from flask import Flask

app = Flask(__name__)

from app.controller import Url_controller
from app.util import Random_generator
from app.repository import Url_repository
