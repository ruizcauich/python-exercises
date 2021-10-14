"""Two kangaroos are trained to jump toward at onece.
The first kangaroo starts at x1 point and moves at 
a rate of v1 meters per jump.
The second Kangaroo starts at x2 and moves at a rate
of v2 meters per jump.

You have to figure out a way to get both kangaroos at
the same location at the same time as part of the show.
If it is possible, return YES, otherwise return NO

Example x1 = 1 v1 = 2
        x2 = 2 v2 = 1
Kangaroos will be at same location at te first jump:
        x1 + v1 = 3
        x2 + v2 = 3

https://www.hackerrank.com/challenges/kangaroo/problem
?isFullScreen=true&h_r=next-challenge
&h_v=zen&h_r=next-challenge&h_v=zen
"""

import math

def kangaroo(x1, v1, x2, v2):
    """Solves the problem using some math tricks.
    Analyasing the problem as a equation problem:

    y = x1 + v1i
    y = x2 + v2i

    Where i is the position where both are at same time
    in meteres (something is not known).

    Doing a substitution of y in the other equation:
    x2 + v2i = x1 + v1i
    x2 - x1 = v1i - v2i

    v1 and v2 are constants so
    x2 - x1 = (v1 - v2)i
    (x2 - x1) / (v1 - v2) = i
    """
    
    # Kangaroos will never be at same place
    # one will always be behind the other
    if x1 > x2 and v1>v2:
        return 'NO'
    
    if x2 > x1 and v2 > v1:
        return 'NO'
    
    
    try:
       intersection_point = (x2 - x1) / (v1 - v2)
    except ZeroDivisionError:
        return 'NO'
    
    # Since the problem takes the movement rate as integers,
    # if the result of the previus operation has a fraction part
    # kangaroos are at same place but their are not on the floor yet
    # A division returns a float number, even if the result 
    # has no fractional portion. So it is important to check
    # 2.0 == float(2) but 2.3 is not 
    is_intersection_point_integer = intersection_point == float(math.floor(intersection_point))
    
    return 'YES' if is_intersection_point_integer else 'NO'


if __name__ == '__main__':

    assert kangaroo(0, 3, 4, 2) == 'YES', 'Should be YES'

    assert kangaroo(0, 2, 5, 3) == 'NO', 'Should be NO'