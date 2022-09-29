answer = int(input("1. Draw your own lines\n2. Use the given shapes\n"))
if answer == 1:
    lines = int(input("How many lines do you wish to draw? "))
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

    print(coordinates)
    with open("coordinates.txt", 'w') as f:
        for line in coordinates:
            for point in line:
                f.write(str(point))
                f.write("\n")

if answer == 2:
    shape = int(input("1. Square\n2.Triangle\n3.Pentagon\n"))
    
