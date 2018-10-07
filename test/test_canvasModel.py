import unittest
import json

from flaskDraw.canvasModel import CanvasModel

class test_canvasModel(unittest.TestCase):
    def setUp(self):
        self.canvasModel = CanvasModel()

    def test_newCanvasModel(self):
        self.assertEqual(720, self.canvasModel.canvas["width"])
        self.assertEqual(480, self.canvasModel.canvas["height"])