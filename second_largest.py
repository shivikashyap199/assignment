#2
n=int(input("enter the elements"))
max1=float('-inf')
max2=float('-inf')
for i in range(1,n+1):
    ele=int(input("enter"))
    if(max1<ele):
        max2=max1
        max1=ele
if(max2==max1):
    print("no second largest")
else:
    print(max2)