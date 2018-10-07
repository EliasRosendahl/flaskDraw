import json


class CanvasModel(object):
    def __init__(self, canvas = 0):
        self.canvas = canvas # property
        self.canvas_ = {
            "width": 720,
            "height": 480,
            "data": dict.fromkeys(range(0, 10), 0)
        }
        # Empty data should be populated using dict comprehension
        

    def get_canvas(self):
        return json.loads(json.dumps(self.canvas_))

    def set_canvas(self, value):
        pass

    canvas = property(get_canvas, set_canvas)