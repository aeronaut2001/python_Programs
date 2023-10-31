a=0
b=1

number =int(input("enter the number :"))

if number == 1:
    print(a)
else :
    print(a)
    print(b)
    for i in range(1,number+1):
        c=a+b
        a = b
        b = c
        print(c)