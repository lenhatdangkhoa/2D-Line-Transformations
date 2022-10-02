import math
import numpy as np # Scientific computing library for Python

"""
Translate the lines by Tx (horizontal displacement) and Ty (vertical displacement)
"""
def basic_translate(Tx, Ty):
    matrix = ([1, 0, 0],
              [0, 1, 0],
              [Tx, Ty, 1])
    return matrix
    
"""
Scale the lines by Sx (horizontal scale) and Sy (vertical scale) assuming the center of scale is at the origin (0,0)
"""
def basic_scale(Sx, Sy):
    matrix = ([Sx, 0, 0],
              [0, Sy, 0],
              [0, 0, 1])
    return matrix

"""
Rotate the lines by "angle" degrees clockwise assuming the center of rotation is at the origin (0,0)
"""
def basic_rotate(angle):
    rad_angle = math.radians(angle)
    matrix = ([math.cos(rad_angle), -1 * math.sin(rad_angle), 0],
              [math.sin(rad_angle), math.cos(rad_angle), 0],
              [0, 0, 1])
    return matrix

"""
Scale the lines by Sx (horizontal scale) and Sy (vertical scale) at the center of scale (Cx, Cy)
"""
def scale(Sx, Sy, Cx, Cy):
    matrix = np.dot(basic_translate(-1*Cx,-1*Cy), basic_scale(Sx,Sy))
    matrix = np.dot(matrix, basic_translate(Cx,Cy))
    return matrix

"""
Rotate the lines by "angle" degrees clockwise at the center of rotation (Cx, Cy)
"""
def rotate(angle, Cx, Cy):
    matrix = np.dot(basic_translate(-1*Cx,-1*Cy), basic_rotate(angle))
    matrix = np.dot(matrix, basic_translate(Cx,Cy))
    return matrix

  