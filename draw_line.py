import math
from PIL import Image
from transformations import *
import math


image = Image.new(mode="RGB", size = (250, 250), color = (0,0,0))

def draw_basic_line(x0, y0, x1, y1):

    # If x0 == x1, in other words, it's a vertical line, just draw a vertical line |y1 - y0| times.
    if x0 == x1:
        smaller_y_value = min(y0,y1)
        # The critical loop
        for i in range(abs(y1 - y0) + 1):
            if (x0 > -1 and x0 < 250) and (smaller_y_value + i > -1 and smaller_y_value + i < 250):
                image.putpixel((x0, smaller_y_value + i), (255,255,255))

    # Else, find the equation of the line using two points and draw a line accordingly
    else:
        slope = (y1 - y0) / (x1 - x0)
        y_intercept = y1 - (slope * x1)

        # If Δx >= Δy, or |x1-x0| >= |y1-y0|, draw horizontally |x1-x0| times.
        if (abs(x1 - x0)) >= (abs(y1-y0)):
            smaller_x_value = min(x0, x1)
            # The critical loop
            for i in range(abs(x1 - x0) + 1):
                x = smaller_x_value + i
                y = (slope * x) + y_intercept
                y = math.trunc(y)
                if (x > -1  and x < 250) and (y > -1 and y < 250):
                    image.putpixel((x,y), (255,255,255))
        # If Δx < Δy, or |x1-x0| < |y1-y0|, draw vertically |y1-y0| times.
        elif (abs(x1-x0)) < (abs(y1-y0)):
            smaller_y_value = min(y0,y1)
            # The critical loop
            for i in range(abs(y1-y0) + 1):
               y = smaller_y_value + i
               x = (y - y_intercept)/slope
               x = math.trunc(x)
               if (x > -1  and x < 250) and (y > -1 and y < 250):
                image.putpixel((x,y), (255,255,255))

def read_coordinates():
    coordinates = []
    with open("coordinates.txt") as f:
        coordinates = f.readlines()
        
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])
    return coordinates

def show_image():
    coordinates = read_coordinates()
    for i in range(0, len(coordinates), 4):
        x0 = coordinates[i]
        y0 = coordinates[i + 1]
        x1 = coordinates[i + 2]
        y1 = coordinates[i + 3]
        draw_basic_line(x0,y0,x1,y1)
    image.show()

def read_new_coordinates():
    coordinates = []
    with open("new_coordinates.txt") as f:
        coordinates = f.readlines()
        
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])
    return coordinates

def show_new_image():
    reset_image()
    coordinates = read_new_coordinates()
    for i in range(0, len(coordinates), 4):
        x0 = coordinates[i]
        y0 = coordinates[i + 1]
        x1 = coordinates[i + 2]
        y1 = coordinates[i + 3]
        draw_basic_line(x0,y0,x1,y1)
    image.show()

def reset_image():
    for y in range(250):
        for x in range(250):
            image.putpixel((x,y), (0,0,0))

