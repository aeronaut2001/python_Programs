
number = int(input("enter the value :"))

if number %2 == 0 :
    print(number,"is even number")
else :
    print(number,"is odd number")


#optimize it in other way is random module

import random
number = random.randint(1,100)

if number %2 == 0 :
    print(number,"is even number")
else :
    print(number,"is odd number")

#more optimization its should run loop of 10 auto

import random

for a in range(10):
    number = random.randint(1, 100)
    if number % 2 == 0:
        print(number, "is even number")
    else:
        print(number, "is odd number")


