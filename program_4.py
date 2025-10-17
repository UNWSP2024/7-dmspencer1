# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

import math

def get_distance(coords1, coords2):
    distance = math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2 + (coords1[2] - coords2[2])**2)

    return distance
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)
try:
    coords1 = (float (input('What is the x value of the first coordinate?: ')),
               float(input('What is the y value of the first coordinate?: ')),
               float(input('What is the z value of the first coordinate?: ')))
    coords2 = (float(input('What is the x value of the second coordinate?: ')),
               float(input('What is the y of the second coordinate?: ')),
               float(input('What is the z of the second coordinate?: ')))

    distance = get_distance(coords1, coords2)

    print(f'The distance between the two coordinates is {distance:,.2f}')

except ValueError:
    print('Invalid input')