
number = int(input("enter the number:"))

for i in range(1,number):
    if number % i == 0:
        print(i,"is factorial of",number)


# little optimization :

number = int(input("enter the number:"))
list = []
for i in range(1, number):
    if number % i == 0:
        print(i, "is factorial of", number)
        list.append(i)


print(list)
