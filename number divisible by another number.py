# #method 1:

number= int(input("enter the number:"))

for t in range(1,100):
    if t% number == 0 :
     print(t)

#method 2 using lamda funn and filter:

num = [12,15,36,25,60,80,95,120]

t=list(filter(lambda x: x % 12 ==0,num))
print(t)