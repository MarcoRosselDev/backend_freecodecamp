""" Write a function called triangle that takes a 
string and an integer and draws a pyramid with the 
given height, made up using copies of the string. 
Here’s an example of a pyramid with 5 levels, using the
 string 'L'. """


def triangle(str, n):
    for i in range(n):
        print(str*(i+1))


triangle('L', 5)
