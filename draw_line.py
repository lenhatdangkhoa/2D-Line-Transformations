import math
from PIL import Image

# Creating a blank dark screen
image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))

def draw_basic_line(x0, y0, x1, y1):
    total_time = 0 # Calculate the run time for the critical loop
    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        # The critical loop
        for i in range(abs(y1 - y0) + 1):
            image.putpixel((x0, smaller_y_value + i), (255,255,255))

    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):
            smaller_x_value = min(x0, x1)
            # The critical loop
            for i in range(abs(x1 - x0)):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                image.putpixel((x,y), (255,255,255))
        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            # The critical loop
            for i in range(abs(y1-y0)):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               image.putpixel((x,y), (255,255,255))

draw_basic_line(25, 25, 25, 50)
draw_basic_line(25, 50, 50, 50)
draw_basic_line(25, 25, 50, 25)
draw_basic_line(50, 25, 50, 50)
image.show()