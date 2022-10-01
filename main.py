from settings import *

answer = input("1) Draw your own lines\n2) Use the given shapes\n")
if answer.strip() == '1':
    lines = int(input("How many lines do you wish to draw? "))
    store_lines(lines)
    prompt_transformation()
elif answer.strip() == '2':
    shape = int(input("1) Square\n2) Triangle\n"))
    if shape == 1:
        store_square()
        prompt_transformation()
    elif shape == 2:
        store_triangle()
        prompt_transformation()
    else:
        print("Invalid answser. Try again.")
else:
    print("Invalid answer. Try again.")
