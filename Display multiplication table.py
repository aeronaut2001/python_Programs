# 1st method using for loop

value_1 = int(input("enter the value :"))
for a in range(1,10+1):
    table = value_1*a
    print("table of",value_1,"is",value_1,"*",a,"=",table)


# 2nd method using while loop
value_1 = int(input("enter the value :"))
i = 1
while i <= 10:
    print(value_1,"*",i,"=",value_1*i)
    i=i+1