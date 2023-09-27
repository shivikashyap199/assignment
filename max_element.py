
#1
n=int(input("enter the numbers"))
max1=float('-inf')
for i in range(1,n+1):
    ele=int(input("enter"))
    if(max1<ele):
        max1=ele
print(max1)



