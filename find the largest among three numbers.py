# a=int(input("enter number a:"))
# b=int(input("enter number b:"))
# c=int(input("enter number c:"))
#
# if a<b<c :
#     print(c,"is bigger number")
# elif a<c<b :
#     print(b,"is a bigger number")
# elif b<c<a :
#     print(a,"is bigger number")
# elif b<a<c :
#     print(c,"is bigger number")
# elif c<b<a :
#     print(a,"is bigger number")
# else  :
#     print(b,"is bigger number")

# 2nd approch easy

a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=int(input("enter number c:"))

if a>b and a>c :
    print(a, "is bigger number")
elif b>c and b>a :
    print(b,"is bigger number")
else :
    print(c, "is bigger number")