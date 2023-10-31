number= int(input("enter the number:"))

sum=0
temp = number

while temp > 0 :
    digit = temp %10
    cube = digit**3
    sum=sum + cube
    temp //= 10  # floor division

if sum == number :
    print("its a armstrong number")
else:
    print("its not a armstrong number")

