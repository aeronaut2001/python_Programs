
number = int(input("Enter the number: "))

if number == 1:
    print(number, "is not a prime number")
else:
    for a in range(2, number):
        if number % a == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
