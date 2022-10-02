from transformations import *
import numpy as np
from draw_line import *

"""
A loop to take user input for coordinates and storing it in coordinates.txt
"""
def store_lines(lines):
    coordinates = []
    for i in range(lines):
        coordinate = []
        print(f'line {i + 1}')
        x0 = int(input("Enter x0: "))
        y0 = int(input("Enter y0: "))
        x1 = int(input("Enter x1: "))
        y1 = int(input("Enter y1: "))
        coordinate.append(x0)
        coordinate.append(y0)
        coordinate.append(x1)
        coordinate.append(y1)
        coordinates.append(coordinate)
    
    with open("coordinates.txt", 'w') as f:
        for line in coordinates:
            for point in line:
                f.write(str(point))
                f.write("\n")
    show_image()

"""
Storing the coordinates of a square into coordinates.txt
"""
def store_square():
    with open("coordinates.txt", 'w') as f:
        f.write(str(25))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(25))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
    show_image()

"""
Storing the coordinates of a triangle into coordinates.txt
"""
def store_triangle():
    with open("coordinates.txt", 'w') as f:
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(100))
        f.write("\n")
        f.write(str(100))
        f.write("\n")
        f.write(str(100))
        f.write("\n")
        f.write(str(100))
        f.write("\n")
        f.write(str(150))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(150))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
        f.write(str(50))
        f.write("\n")
    show_image()
    
"""
The main loop for the user to apply transformations
"""
def prompt_transformation():
    coordinates = []
    with open("coordinates.txt") as f:
        coordinates = f.readlines()
    
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])

    ans = 0 # Placeholder
    while ans != '4':
        ans = input("1) Translate\n2) Scale\n3) Rotate\n4) Quit\n")

        if ans.strip() == '1':
            x_dis = int(input("x displacements) "))
            y_dis = int(input("y displacements) "))
            translate_matrix = basic_translate(x_dis, y_dis)
            new_coordinates =[]

            for i in range(0, len(coordinates), 4):
                temp = []
                x0 = coordinates[i]
                y0 = coordinates[i + 1]
                x1 = coordinates[i + 2]
                y1 = coordinates[i + 3]
                point_matrix1 = [x0,y0,1]
                point_matrix2 = [x1,y1,1]
                result_matrix1 = np.dot(point_matrix1,translate_matrix)
                result_matrix2 = np.dot(point_matrix2,translate_matrix)
                temp.append(round(result_matrix1[0]))
                temp.append(round(result_matrix1[1]))
                temp.append(round(result_matrix2[0]))
                temp.append(round(result_matrix2[1]))
                new_coordinates.append(temp)

            # Writing coordinates to a new coordinates file
            with open("new_coordinates.txt", 'w') as f:
                for line in new_coordinates:
                    for point in line:
                        f.write(str(point))
                        f.write("\n")

            show_new_image()

        elif ans.strip() == '2':
            x_scale = float(input("x scaling factor) "))
            y_scale = float(input("y scaling factor) "))
            xC, yC = input("Center of scale) ").split()
            scaling_matrix = scale(x_scale, y_scale, int(xC), int(yC))
            new_coordinates =[]

            for i in range(0, len(coordinates), 4):
                temp = []
                x0 = coordinates[i]
                y0 = coordinates[i + 1]
                x1 = coordinates[i + 2]
                y1 = coordinates[i + 3]
                point_matrix1 = [x0,y0,1]
                point_matrix2 = [x1,y1,1]
                result_matrix1 = np.dot(point_matrix1,scaling_matrix)
                result_matrix2 = np.dot(point_matrix2,scaling_matrix)
                temp.append(round(result_matrix1[0]))
                temp.append(round(result_matrix1[1]))
                temp.append(round(result_matrix2[0]))
                temp.append(round(result_matrix2[1]))
                new_coordinates.append(temp)

            # Writing coordinates to a new coordinates file
            with open("new_coordinates.txt", 'w') as f:
                for line in new_coordinates:
                    for point in line:
                        f.write(str(point))
                        f.write("\n")

            show_new_image()

        elif ans.strip() == '3':
            angle = float(input("Angle of rotation) "))
            xR, yR = input("Center of rotation) ").split()
            rotation_matrix = rotate(angle, int(xR), int(yR))
            new_coordinates =[]

            for i in range(0, len(coordinates), 4):
                temp = []
                x0 = coordinates[i]
                y0 = coordinates[i + 1]
                x1 = coordinates[i + 2]
                y1 = coordinates[i + 3]
                point_matrix1 = [x0,y0,1]
                point_matrix2 = [x1,y1,1]
                result_matrix1 = np.dot(point_matrix1,rotation_matrix)
                result_matrix2 = np.dot(point_matrix2,rotation_matrix)
                temp.append(round(result_matrix1[0]))
                temp.append(round(result_matrix1[1]))
                temp.append(round(result_matrix2[0]))
                temp.append(round(result_matrix2[1]))
                new_coordinates.append(temp)
            
            # Writing coordinates to a new coordinates file
            with open("new_coordinates.txt", 'w') as f:
                for line in new_coordinates:
                    for point in line:
                        f.write(str(point))
                        f.write("\n")

            show_new_image()
        
    
