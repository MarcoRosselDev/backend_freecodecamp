""" Write a function named print_right that takes a string named text as a parameter 
and prints the string with enough leading spaces that the last letter of the string 
is in the 40th column of the display.

Hint: Use the len function, the string concatenation operator (+) and the string 
repetition operator (*).

Here’s an example that shows how it should work. 

print_right("Monty")
print_right("Python's")
print_right("Flying Circus")

                                   Monty
                                Python's
                           Flying Circus
"""


def print_right(text):
    add = ""
    for i in range(40 - len(text)):
        add += " "
    add += text
    print(add)


print_right("Hola")
print_right("another test")
