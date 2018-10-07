import unittest
import json

from flaskDraw.canvasModel import CanvasModel

class test_canvasModel(unittest.TestCase):
    def setUp(self):
        self.canvasModel = CanvasModel()

    def test_newCanvasModel(self):
        testImgData = json.loads('{"width": "720", "height": "480", "data": "{}"}')
        self.assertEqual(testImgData, self.canvasModel.canvas)