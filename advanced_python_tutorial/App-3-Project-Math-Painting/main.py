import numpy as np
from PIL import Image
from datetime import datetime

# black: data[:] = [0, 0, 0]
# white: data[:] = [255, 255, 255]

class Canvas:

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        self.canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.canvas[:] = color

    def make(self):
        current_time = datetime.now()
        img = Image.fromarray(self.canvas, 'RGB')
        img.save(f"images/canvas_{current_time.strftime('%Y%m%d_%H%M%S')}.png")

    def canvas(self):
        return self.canvas


class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas[self.x:self.x+self.side, self.y:self.y+self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas[self.x:self.x+self.height, self.y:self.y+self.width] = self.color


canv = Canvas(100, 100, [255, 255, 255])
square = Square(44, 28, 40, [255, 0, 0])
square.draw(canv.canvas)
rect1 = Rectangle(50, 55, 40, 24, [0, 0, 0])
rect1.draw(canv.canvas)

canv.make()






#
#
# class Rectangle:
#
#     def __init__(self, x, y, width, height, color):
#         self.color = color
#         self.height = height
#         self.side = width
#         self.y = y
#         self.x = x
#
#     def draw(self, canvas):
#         pass

# def make(self):
#     canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
#
#     if self.color.lower() == "white":
#         canvas[:] = [255, 255, 255]
#         img = Image.fromarray(canvas, 'RGB')
#         img.save('images/test_canvas.png')
#     elif self.color.lower() == 'black':
#         canvas[:] = [0, 0, 0]
#         img = Image.fromarray(canvas, 'RGB')
#         img.save('images/test_canvas.png')
#     else:
#         print("Wrong canvas color! Only 'white' or 'black' are available!")