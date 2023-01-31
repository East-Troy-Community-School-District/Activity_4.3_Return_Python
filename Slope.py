'''
Slope
1/30/2023
Python I

Instructions:
Read through the code so you understand how the
program works. Currently, the program is missing
a call to the function slope(). Add a call so
that the program calculates and displays the
slope of a line defined by (2, 4) and (7, -2).
'''

def slope(x1, y1, x2, y2):
    '''
    Returns the slope of a line defined by the two points.
    '''
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Add your call here!
