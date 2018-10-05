from flask import Flask
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

from flaskDraw.canvasView import renderCanvas

@app.route("/")
def index():
    return renderCanvas("foo")

@socketio.on('diff')
def diff(imgDataDiff):
    emit('new diff', imgDataDiff, broadcast='false')


if __name__ == '__main__':
    app.run()