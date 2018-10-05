import unittest
from unittest import mock

from flaskDraw.canvasModel import CanvasModel
from .flaskDraw.canvasView import renderCanvas
class test_canvasView(unittest.TestCase):
    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(1, 1)

    @mock.patch('canvasView.render_template')
    def test_renderCanvas(self, mock_render):
        renderCanvas()
        mock_render.canvasView.assert_called_with("index.html")
