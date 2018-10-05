from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

from flaskDraw.canvasView import renderCanvas

@app.route("/")
def index():
    return renderCanvas("foo")


if __name__ == '__main__':
    app.run()