"""
   Print multiplication table (Spec sheet).
    :param start: the inclusive start of the table
    :param end: the exclusive end of the table
    :param shape: if 0, print the whole square; if 1, print lower triangle
    :return: None
    :raises: ValueError if start > end
    """

#enum 

from enum import Enum

class Shape(Enum):
    Square = 0
    Lower_Triangle = 1
    Upper_Triangle = 2


#check type first ALWAYS because... you assume type if you check value first
def printmult_table(start, end, shape =0):

    if start > end:
        raise ValueError("Err, start < end")
    if start < 0:
        raise ValueError("Err, no negative numbers")
    if end < 0:
        raise ValueError("Err, no negative numbers")
    
    n = [0,1]

    if shape not in n:
        raise ValueError("shape value must be either 1 or 0")

    if shape == 0:
        return rectangle(start,end)
    
    if shape == 1:
        return triangle(start,end)


#by defining these functions outside of the class we can safely call them when returning rectangle
#or triangle depending on the hsa[e]
# Rectangle
def rectangle(start,end):
    for x in range(start, end):
        for y in range(start, end):
            print(f"{x * y:2}", end=' ')
        print()
    print()

# Lower triangle
def triangle(start,end):
    for i in range(start, end):
        for j in range(start, i + 1):
            print(f"{i * j:2}", end=' ')
        print()

print(printmult_table(1,10,1))






