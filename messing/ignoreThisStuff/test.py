
import math

#Takes a floating number input from user:
float_number = float(input("Please enter a positive number:   "))
print (float_number)


def sqrt(x):
    print("in this")
    squareroot = (x ** (1.0/2))
    print ("approx = {}".format(squareroot))
    return squareroot

print("The square root of", str(float_number) + " is approx.", str(round(sqrt(float_number), 1)))

