'''
Return Area
1/30/2023
Python I

Instructions:
Trace the program to determine how it executes and
what it displays. Check your work by running the program.
Finally, let's discuss the following questions...
1. What is the advantage to return the area instead of
   automatically printing it?
2. What happens if you add the following line of code
   to the program?

area(8, 8)

'''


def area(length, width):
    '''
    Returns the area of a rectangle.
    '''
    area = length * width
    return area


print(area(2, 3))
print("Area: " + str(area(5, 6)))
total_area = area(9, 9) + area(7, 5)
print("Total area of rectangle: " + str(total_area))