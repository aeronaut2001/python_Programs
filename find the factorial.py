# 1st method with for loop :

number = int(input("enter the number :"))
factorial = 1

if number <0 :
    print("it not exists")
if number == 0:
    print("factorial of 0 is",1)
if number >0 :
    for a in range(1,number+1):
        factorial=factorial*a

print("factorial of",number,"is",factorial)


# 2nd method with recursive :

def factorial(a):
    if a== 0:
        return 1
    else :
        return ((a)*factorial(a-1))

number = int(input("enter the number :"))
result = factorial(number)
print("factorial of",number,"is",result)
