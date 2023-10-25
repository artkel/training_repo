from canvas import Canvas
from shapes import Square, Rectangle

canv_width = int(input("Enter canvas width in pixels: "))
canv_height = int(input("Enter canvas height in pixels: "))
canv_color = input("Choose canvas color, black or white: ")

colors = {'black': [0, 0, 0], 'white': [255, 255, 255]}

canv = Canvas(canv_width, canv_height, colors[canv_color.lower()])

while True:
    next_object = input("Choose next object to draw, 'square' or 'rectangle'. Type 'quit' to finish. ")

    if next_object.lower() == 'square':
        # Ask for new square properties
        square_x = int(input("Enter square x-origin: "))
        square_y = int(input("Enter square y-origin: "))
        square_side = int(input("Enter square side length in pixels: "))
        square_r = int(input("Enter value between 0 and 255 to define square red depth: "))
        square_g = int(input("Enter value between 0 and 255 to define square green depth: "))
        square_b = int(input("Enter value between 0 and 255 to define square blue depth: "))

        square = Square(square_x, square_y, square_side, [square_r, square_g, square_b])
        square.draw(canv)

    elif next_object.lower() == 'rectangle':
        # Ask for new rectangle properties
        rectangle_x = int(input("Enter rectangle x-origin: "))
        rectangle_y = int(input("Enter rectangle y-origin: "))
        rectangle_width = int(input("Enter rectangle width in pixels: "))
        rectangle_height = int(input("Enter rectangle height in pixels: "))
        rectangle_r = int(input("Enter value between 0 and 255 to define rectangle red depth: "))
        rectangle_g = int(input("Enter value between 0 and 255 to define rectangle green depth: "))
        rectangle_b = int(input("Enter value between 0 and 255 to define rectangle blue depth: "))

        rectangle = Rectangle(rectangle_x, rectangle_y, rectangle_width, rectangle_height,
                              [rectangle_r, rectangle_g, rectangle_b])
        rectangle.draw(canv)

    elif next_object.lower() == 'quit':
        break

canv.make()