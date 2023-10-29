import math

#1st method

a= float(input("enter square root value:"))
squareroot = a**0.5       # ** consider as power of a its like  a^0.5

print("square root is:",squareroot)



#2nd method

from math import sqrt

a=float(input("enter square root value:"))

squareroot = math.sqrt(a)

print("square root is:",squareroot)
