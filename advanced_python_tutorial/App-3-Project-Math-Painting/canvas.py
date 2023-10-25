from datetime import datetime

import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = color

    def make(self):
        current_time = datetime.now()
        img = Image.fromarray(self.data, 'RGB')
        img.save(f"images/canvas_{current_time.strftime('%Y%m%d_%H%M%S')}.png")

    # def canvas(self):
    #     return self.canvas