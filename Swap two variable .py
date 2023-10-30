# 1st method with 3rd variable

a=2
b=4

temp =b

b=a
print("b= ",b)

a=temp

print("a= ",a)

# 2nd method without third variable

a=2
b=4

a,b=b,a

print("a=",a)
print("b=",b)