from flask import Flask
from flask_socketio import SocketIO
from .boxoffice import *


app = Flask(__name__)
socketio = SocketIO(app)

socketio.on_namespace(BoxOffice('/boxoffice'))
