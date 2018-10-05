from flask import Flask
app = Flask(__name__)

from flaskDraw.flaskDraw.canvasView import renderCanvas

@app.route("/")
def index():
    return renderCanvas("foo")
