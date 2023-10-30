#quadratic equation is a** + bx +c = 0
# a,b,c are the real numbers
# a!= 0

import cmath
a=int(input("enter value of a!= 0 :"))
if a != 0 :
        print(a)
else :
        exit()


b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

# formula for discriminent

d = (b**2) - (4*a*c)

root_1 = (-b+cmath.sqrt(d))/(2*a)
root_2 = (-b-cmath.sqrt(d))/(2*a)

print('positive root - ',root_1 ,'\n','negative root -',root_2)