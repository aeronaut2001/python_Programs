a=int(input("enter the number:"))
b=int(input("enter the number:"))
List = str(input(["+","-","*","/"]))


if List == "+":
        print("sum =",a+b)
elif List == "-":
        print("sub =",a-b)
elif List == "*":
        print("mul =",a*b)
elif List == "/":
        print("div =",a/b)
else :
        print("error")
